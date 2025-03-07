# utils.py

This is a Python utility file named `utils.py`. It contains two main functions: `make_dir` and `create_scatterplot_and_save`. The file is primarily used for creating directories and generating scatter plots from a given DataFrame.

## Import Statements

The file begins with import statements for the `os`, `seaborn`, and `matplotlib.pyplot` modules. 

- `os` is a standard Python library for interacting with the operating system.
- `seaborn` and `matplotlib.pyplot` are popular data visualization libraries in Python.

## Function: make_dir

```python
def make_dir(dir) -> None:
    if not os.path.exists(dir):
        os.makedirs(dir)
```

This function takes a single parameter, `dir`, which is the path of the directory to be created. If the directory does not already exist, it is created using the `os.makedirs` function.

### Example

```python
make_dir('/path/to/directory')
```

This will create a directory at the specified path if it does not already exist.

## Function: create_scatterplot_and_save

```python
def create_scatterplot_and_save(df, x, y, file_path) -> None:
    plt.rcParams["font.family"] = "SF Compact Text"
    font_scale = 2
    sns.set(font_scale=font_scale, font="SF Compact Text")

    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x, y=y, alpha=0.7)
    plt.axhline(y=0, color="red", linestyle="--")
    plt.xlabel("Cost")
    plt.ylabel("Residuals")
    plt.tight_layout()
    plt.savefig(file_path)
```

This function creates a scatter plot from a DataFrame and saves it to a specified file path. It takes four parameters:

- `df`: The DataFrame containing the data to be plotted.
- `x`: The column in the DataFrame to be used for the x-axis.
- `y`: The column in the DataFrame to be used for the y-axis.
- `file_path`: The path where the plot will be saved.

The function first sets the font family and scale for the plot. It then creates a scatter plot with the specified x and y data, adds a horizontal line at y=0, labels the x and y axes, adjusts the layout to fit the plot neatly within the figure, and finally saves the figure to the specified file path.

### Example

```python
create_scatterplot_and_save(df, 'cost', 'residuals', '/path/to/save/plot.png')
```

This will create a scatter plot with 'cost' on the x-axis and 'residuals' on the y-axis, and save the plot as a PNG file at the specified path.