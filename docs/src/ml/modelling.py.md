# modelling.py

This Python file contains the implementation of a machine learning model for solving puzzles. The file includes the definition of a custom PyTorch Dataset class, a PyTorch Model class, and a training function. The code uses PyTorch for model definition, training, and inference, and pandas for data manipulation.

## PuzzleDataset Class

This class is a custom implementation of the PyTorch Dataset class. It is used to load the puzzle data and make it available to the PyTorch DataLoader.

### Methods

- `__init__(self, data) -> None`: This method initializes the PuzzleDataset object. It takes a pandas DataFrame `data` as input, which should contain the puzzle data.

- `__len__(self) -> int`: This method returns the number of samples in the dataset.

- `__getitem__(self, idx) -> tuple[Tensor, Tensor]`: This method returns the `idx`-th sample from the dataset. The sample is returned as a tuple of two PyTorch tensors: the state of the puzzle and the cost of the puzzle.

## PuzzleHeuristicModel Class

This class is a custom implementation of the PyTorch Module class. It defines a neural network model for predicting the cost of a puzzle given its state.

### Methods

- `__init__(self, input_size, hidden_sizes) -> None`: This method initializes the PuzzleHeuristicModel object. It takes two arguments: `input_size`, which is the size of the input tensor, and `hidden_sizes`, which is a list of integers representing the sizes of the hidden layers in the network.

- `forward(self, x: Tensor) -> Tensor`: This method defines the forward pass of the network. It takes a PyTorch tensor `x` as input and returns a PyTorch tensor as output.

## train Function

This function trains the PuzzleHeuristicModel on the puzzle data. It takes five arguments: `input_file_path`, `save_model_dir`, `run_name`, `n`, and `should_stratify`.

### Parameters

- `input_file_path: str`: The path to the CSV file containing the puzzle data.
- `save_model_dir: str`: The directory where the trained model should be saved.
- `run_name: str`: The name of the training run. This is used to create a subdirectory in `save_model_dir` where the logs and model weights for this run will be saved.
- `n: int`: The number of rows to read from the CSV file. If `n` is less than or equal to 0, all rows are read.
- `should_stratify: bool`: Whether to stratify the train-test split. If `True`, the split is stratified based on the 'cost' column of the data.

### Return

- `None`

## Technical Concepts

- PyTorch: PyTorch is an open-source machine learning library based on the Torch library. It is used for applications such as computer vision and