import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import pandas as pd
from sklearn.model_selection import train_test_split
import torch.nn.functional as F
import numpy as np


def train():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load the data
    data = pd.read_csv("data/input/fifteen-puzzle-6M.csv")
    data = data[data["cost"] < 70]

    # Split data into 70% training and 30% remaining (test + validation)
    train_data, remaining_data = train_test_split(
        data, test_size=0.3, stratify=data["cost"], random_state=42
    )

    # Split the remaining 30% into 50% test and 50% validation
    test_data, val_data = train_test_split(
        remaining_data, test_size=0.5, stratify=remaining_data["cost"], random_state=42
    )

    # Display the sizes of each split
    print(f"Train data size: {len(train_data)}")
    print(f"Test data size: {len(test_data)}")
    print(f"Validation data size: {len(val_data)}")

    class PuzzleDataset(Dataset):
        def __init__(self, data):
            self.data = data

        def __len__(self):
            return len(self.data)

        def __getitem__(self, idx):
            state = torch.tensor(self.data.iloc[idx, :-1].values, dtype=torch.float32)
            state_one_hot = torch.tensor(
                np.eye(16)[state.to(torch.int64)].ravel(), dtype=torch.float32
            )
            cost = torch.tensor(self.data.iloc[idx, -1], dtype=torch.float32)
            return state_one_hot, cost

    batch_size = 64
    train_dataset = PuzzleDataset(train_data)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    test_dataset = PuzzleDataset(test_data)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    val_dataset = PuzzleDataset(val_data)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    class PuzzleHeuristicModel(nn.Module):
        def __init__(self, input_size, hidden_sizes):
            super(PuzzleHeuristicModel, self).__init__()
            all_sizes = [input_size] + hidden_sizes + [1]
            self.hidden_layers = nn.ModuleList(
                [nn.Linear(all_sizes[i], all_sizes[i + 1]) for i in range(len(all_sizes) - 1)]
            )

        def forward(self, x):
            for layer in self.hidden_layers[:-1]:
                x = F.relu(layer(x))
            x = self.hidden_layers[-1](x)
            return x

    input_size = 256
    hidden_sizes = [1024, 1024, 512, 128, 64]

    model = PuzzleHeuristicModel(input_size, hidden_sizes)

    if torch.cuda.device_count() > 1:
        model = nn.DataParallel(model)
    model.to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.MSELoss()

    num_epochs = 10
    best_loss = float("inf")
    best_model_path = "data/immediate/best_puzzle_model.pth"

    for epoch in range(num_epochs):
        model.train()
        for inputs, targets in train_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets.view(-1, 1))
            loss.backward()
            optimizer.step()

        # Validation
        model.eval()
        with torch.no_grad():
            val_loss = 0.0
            for inputs, targets in val_loader:
                inputs, targets = inputs.to(device), targets.to(device)
                outputs = model(inputs)
                val_loss += criterion(outputs, targets.view(-1, 1)).item()
            val_loss /= len(val_loader)  # Average validation loss

        print(f"Epoch {epoch+1}/{num_epochs}, Validation Loss: {val_loss}")

        # Save the best model based on validation loss
        if val_loss < best_loss:
            best_loss = val_loss
            torch.save(model.state_dict(), best_model_path)

    # Load the best model for testing
    best_model = nn.DataParallel(model)
    best_model.to(device)
    best_model.load_state_dict(torch.load(best_model_path))

    # Testing
    test_loss = 0.0
    best_model.eval()
    with torch.no_grad():
        for inputs, targets in test_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = best_model(inputs)
            test_loss += criterion(outputs, targets.view(-1, 1)).item()
    test_loss /= len(test_loader)  # Average test loss

    print(f"Final Test Loss: {test_loss}")

    model_path = "data/weights/puzzle_model.pth"
    torch.save(best_model.state_dict(), model_path)
