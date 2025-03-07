# inferring.py

This is a Python script that uses PyTorch to define and use a neural network model for solving puzzles. The script contains a class definition for the model, as well as functions for loading the model, making single inferences, and making batch inferences.

## PuzzleHeuristicModel Class

This class defines a neural network model for solving puzzles. It inherits from the `nn.Module` class in PyTorch.

### `__init__(self, input_size, hidden_sizes) -> None`

This is the constructor method for the `PuzzleHeuristicModel` class. It takes two parameters:

- `input_size`: An integer that specifies the size of the input layer of the neural network.
- `hidden_sizes`: A list of integers that specifies the sizes of the hidden layers of the neural network.

The method initializes the hidden layers of the neural network using the `nn.Linear` class from PyTorch.

### `forward(self, x)`

This method defines the forward pass of the neural network. It takes one parameter:

- `x`: A tensor that represents the input to the neural network.

The method applies the ReLU activation function to the outputs of all hidden layers except the last one, and returns the output of the last hidden layer.

## Functions

### `get_model(model_path: str = "data/models/puzzle_model.pth") -> nn.Module`

This function loads a pre-trained `PuzzleHeuristicModel` from a file. It takes one optional parameter:

- `model_path`: A string that specifies the path to the file that contains the pre-trained model. The default value is `"data/models/puzzle_model.pth"`.

The function returns the loaded model.

### `infer(input_data: list[int], model: PuzzleHeuristicModel) -> int`

This function makes a single inference using a `PuzzleHeuristicModel`. It takes two parameters:

- `input_data`: A list of integers that represents the input to the model.
- `model`: A `PuzzleHeuristicModel` that will make the inference.

The function returns the predicted value as an integer.

### `batch_infer(dataframe, model, batch_size=64) -> list[int]`

This function makes batch inferences using a `PuzzleHeuristicModel`. It takes three parameters:

- `dataframe`: A pandas DataFrame that contains the input data. Each row of the DataFrame represents one input.
- `model`: A `PuzzleHeuristicModel` that will make the inferences.
- `batch_size`: An optional integer that specifies the size of the batches. The default value is `64`.

The function returns a list of predicted values. Each value corresponds to one row of the input DataFrame.