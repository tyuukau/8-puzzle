# algorithm_exp.py

This Python script, `algorithm_exp.py`, is used to conduct experiments on different search algorithms and heuristics. It uses the pandas library to handle data, tqdm for progress bars, and multiprocessing for parallel processing. The script imports several classes and functions from other modules, including `InformedSearchAlgorithm`, `GameConfig`, `State`, `AStar`, `GBFS`, `CallableHeuristicClass`, `manhattan_distance`, `ann_distance`, `Game`, and `ResultRecord`.

## Functions

### play_on_one

```python
def play_on_one(
    start_board: list[int], algorithm: InformedSearchAlgorithm, heuristic_func
) -> ResultRecord:
```

This function takes a starting board configuration, a search algorithm, and a heuristic function as input. It creates a game configuration with the starting state, initializes the algorithm with the heuristic, and creates a game instance. The game is then played, and the result is returned.

Parameters:
- `start_board`: A list of integers representing the starting board configuration.
- `algorithm`: An instance of `InformedSearchAlgorithm` to be used for the game.
- `heuristic_func`: A heuristic function to be used by the algorithm.

Returns:
- `ResultRecord`: A record of the game result.

### conduct_algorithm_heuristic_experiment

```python
def conduct_algorithm_heuristic_experiment(
    df: pd.DataFrame,
    algorithm: InformedSearchAlgorithm,
    heuristic: CallableHeuristicClass,
    experiment_folder_path: str,
) -> pd.DataFrame:
```

This function iterates over each row of a DataFrame, plays a game with the given algorithm and heuristic, and updates the DataFrame with the results. The updated DataFrame is then saved as a CSV file in the specified folder.

Parameters:
- `df`: A pandas DataFrame containing the data for the experiment.
- `algorithm`: An instance of `InformedSearchAlgorithm` to be used for the game.
- `heuristic`: An instance of `CallableHeuristicClass` to be used by the algorithm.
- `experiment_folder_path`: A string representing the path to the folder where the experiment results will be saved.

Returns:
- `pd.DataFrame`: The updated DataFrame.

### conduct_algorithm_heuristic_experiment_

```python
def conduct_algorithm_heuristic_experiment_(
    df: pd.DataFrame,
    algorithm: InformedSearchAlgorithm,
    heuristic: CallableHeuristicClass,
) -> pd.DataFrame:
```

This function is similar to `conduct_algorithm_heuristic_experiment`, but it does not save the results to a CSV file.

### experiment_on_part

```python
def experiment_on_part(experiment_folder_path, part) -> pd.DataFrame:
```

This function conducts an experiment on a part of the data using the GBFS algorithm and the manhattan distance heuristic. It returns the updated DataFrame.

Parameters:
- `experiment_folder_path`: A string representing the path to the folder where the experiment results will be saved.
- `part`: A part of the data on which the experiment will be conducted.

Returns:
- `pd.DataFrame`: The updated DataFrame.

### conduct_algorithm_experiment

```python
def conduct_algorithm_experiment(
    experiment_data_path: str,
    experiment_folder_path: str,
    n: int = 0,
) -> None:
```

This function reads the experiment data from a CSV file, shuffles it, splits it into six parts, and conducts an experiment on each part concurrently using the GBFS algorithm and the manhattan distance heuristic. The results are then merged and saved as a CSV file.

Parameters:
- `experiment_data_path`: A string representing the path to the CSV file containing the experiment data.
- `experiment_folder_path`: A string representing the path to the folder where the experiment results will be saved.
- `n`: An integer representing the number of rows to read from the CSV file. If `n` is 0, all rows are read.

Returns:
- None