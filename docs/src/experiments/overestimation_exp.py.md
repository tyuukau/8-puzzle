# overestimation_exp.py

## Overview
This Python script, `overestimation_exp.py`, is designed to conduct an overestimation experiment on a given dataset. The script reads a CSV file, applies a machine learning model to infer predictions, calculates residuals, and creates a scatter plot of the residuals. It also calculates the percentage of overestimated instances and saves the results to a CSV file.

## Usage
To use this script, you need to call the `conduct_overestimation_experiment` function with the appropriate parameters. Here is an example:

```python
from overestimation_exp import conduct_overestimation_experiment

conduct_overestimation_experiment('path_to_input_file.csv', 'path_to_experiment_folder', 1000)
```

## Function: conduct_overestimation_experiment

```python
def conduct_overestimation_experiment(
    input_file_path: str, experiment_folder_path: str, n: int = 0
) -> None:
```

This function conducts the overestimation experiment.

### Parameters

- `input_file_path` (str): The path to the input CSV file.
- `experiment_folder_path` (str): The path to the folder where the experiment results will be saved.
- `n` (int, optional): The number of rows to read from the input file. If `n` is greater than 0, the function will read the first `n` rows. If `n` is 0 or not provided, the function will read all rows.

### Description

The function first creates the experiment folder if it does not exist. Then it reads the input CSV file. If `n` is greater than 0, it reads the first `n` rows; otherwise, it reads all rows. The function then removes duplicate rows.

Next, it applies a machine learning model to the data to infer predictions and adds these predictions to the dataframe as a new column, `predicted_cost`.

The function then creates a list of column names from '0' to '15' and removes any duplicate rows based on these columns.

The function calculates the residuals by subtracting the actual cost from the predicted cost and adds these residuals to the dataframe as a new column, `ann_residual`.

The function then creates a scatter plot of the residuals and saves it to the experiment folder.

Finally, the function calculates the percentage of instances where the predicted cost is greater than the actual cost (overestimation) and prints this percentage. It also saves the dataframe with the predictions and residuals to a CSV file in the experiment folder.

## Dependencies

This script depends on the following Python libraries:

- pandas
- ..utils
- ..ml

The `..utils` library should contain the `create_scatterplot_and_save` and `make_dir` functions. The `..ml` library should contain the `get_model` and `batch_infer` functions.