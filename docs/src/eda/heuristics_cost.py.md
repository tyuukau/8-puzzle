# heuristics_cost.py

## Overview
The `heuristics_cost.py` file is a Python script that is used to evaluate heuristic functions on a dataset. The script uses two heuristic functions, Manhattan distance and Mistile distance, to estimate the cost of reaching a goal state from a given state in a 15-puzzle problem. The script reads a dataset from a CSV file, applies the heuristic functions to each state in the dataset, calculates the residuals, and saves the results to a new CSV file. It also creates and saves scatter plots of the residuals.

## Dependencies
The script uses the following Python libraries:
- pandas: for data manipulation and analysis
- tqdm: for showing progress bars

It also uses the following modules from the same project:
- utils: for creating scatter plots and directories
- heuristics: for the Manhattan distance and Mistile distance functions
- state: for the State class

## Functions

### _calculate_manhattan(row) -> int
This function calculates the Manhattan distance between a given state and the normal state. The state is represented by the first 16 values in the row.

Parameters:
- row: A row from a pandas DataFrame. The first 16 values represent a state in the 15-puzzle problem.

Returns:
- The Manhattan distance between the given state and the normal state.

### _calculate_mistile(row) -> int
This function calculates the Mistile distance between a given state and the normal state. The state is represented by the first 16 values in the row.

Parameters:
- row: A row from a pandas DataFrame. The first 16 values represent a state in the 15-puzzle problem.

Returns:
- The Mistile distance between the given state and the normal state.

### evaluate_heuristics_on_dataset(input_file_path: str, eda_folder_dir: str, n: int = 0) -> None
This function evaluates the Manhattan distance and Mistile distance heuristic functions on a dataset. The dataset is read from a CSV file. The function applies the heuristic functions to each state in the dataset, calculates the residuals, and saves the results to a new CSV file. It also creates and saves scatter plots of the residuals.

Parameters:
- input_file_path: The path to the input CSV file.
- eda_folder_dir: The directory where the output CSV file and scatter plots will be saved.
- n: The number of rows to read from the input CSV file. If n is 0, all rows are read.

Returns:
- None

## Usage
To use the `evaluate_heuristics_on_dataset` function, you need to provide the path to the input CSV file and the directory where the output CSV file and scatter plots will be saved. You can also optionally provide the number of rows to read from the input CSV file.

Example:
```python
evaluate_heuristics_on_dataset('path/to/input.csv', 'path/to/output/directory/', 1000)
```

This will read the first 1000 rows from `input.csv`, apply the heuristic functions to each state, calculate the residuals, save the results to `estimations.csv` in the output directory, and create scatter plots of the residuals.