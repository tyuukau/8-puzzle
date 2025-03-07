# exp_dataset.py

This is a Python script file named `exp_dataset.py`. The script is used to create an experimental dataset from existing data. It uses the pandas and numpy libraries to manipulate data and the warnings library to handle warnings.

## Description

The script reads two CSV files, removes duplicates from the first file, and merges it with the second file. It then selects specific rows based on a cost value and calculates a range of residuals for each cost. For each residual value, it selects the 20 nearest rows and appends them to the result DataFrame. The final DataFrame is then saved as a CSV file.

## Usage

To use this script, simply run it in a Python environment where pandas and numpy are installed. No arguments are required.

## Methods

### make_exp_dataset()

This is the main function of the script. It does not take any parameters.

#### Description

The function first suppresses FutureWarning warnings. It then reads two CSV files into pandas DataFrames. The first DataFrame is deduplicated and reset. The two DataFrames are then concatenated along the columns, and any duplicate columns are removed.

The function then defines a list of selected costs and two variables for the number of residual values and the number of nearest rows. An empty DataFrame is created to store the results.

A loop is then started over the selected costs. For each cost, the function filters the merged DataFrame and calculates a range of residuals. It then creates an array of evenly spaced residual values within the range. For each residual value, it selects the 20 nearest rows and appends them to the result DataFrame.

Finally, the function selects specific columns from the result DataFrame, converts the data to integers, and saves the DataFrame as a CSV file.

#### Parameters

This function does not take any parameters.

## Technical Concepts

The script uses the pandas library for data manipulation and the numpy library for numerical operations. It uses the `read_csv`, `drop_duplicates`, `reset_index`, `concat`, `loc`, `abs`, `argsort`, `astype`, and `to_csv` methods from pandas and the `linspace` function from numpy.

The script also uses list comprehension, for loops, and the `filterwarnings` function from the warnings library. It uses the `copy` method to avoid the SettingWithCopyWarning in pandas.

## File Content

The file content is a Python script that creates an experimental dataset from existing data. It reads data from two CSV files, manipulates the data, and saves the result as a new CSV file. The script is well-structured and uses several advanced features of the pandas and numpy libraries.