# game_config.py

This is a Python code file that defines a class `GameConfig` which is used to store the configuration of a game. The class has several attributes and methods that are used to manipulate and validate the game configuration.

## Class: GameConfig

The `GameConfig` class is used to store the configuration of a game. It has the following attributes:

- `width` (`int`): Width of the square puzzle grid.
- `start_state` (`State`): Initial state of the puzzle represented as a tuple of integers.
- `goal_state` (`State`): Goal state of the puzzle represented as a tuple of integers.
- `solvable` (`bool`): A boolean indicating if the puzzle is solvable. Calculated using `self._is_solvable()`.

### Example

```python
game_config = GameConfig(
    start_state=State(3, 7, 4, 8, 5, 6, 2, 0, 1),
    goal_state=State(0, 1, 2, 3, 4, 5, 6, 7, 8),
)
```

### Methods

#### `__init__(self, start_state: State, goal_state: State) -> None`

This is the constructor method for the `GameConfig` class. It initializes the `width`, `start_state`, `goal_state` attributes and validates the data using the `_validate_data` method.

Parameters:

- `start_state` (`State`): Initial state of the puzzle represented as a tuple of integers.
- `goal_state` (`State`): Goal state of the puzzle represented as a tuple of integers.

#### `__str__(self) -> str`

This method returns a string representation of the `GameConfig` object.

#### `_validate_data(self) -> None`

This private method validates the data of the `GameConfig` object. It checks if the width of the start and goal states are consistent. If not, it raises a `ValueError`.

#### `_count_inversions(self, numbers: tuple[int]) -> int`

This private method counts the number of inversions in a given tuple of numbers. An inversion is a pair of numbers where the number on the left is greater than the number on the right.

Parameters:

- `numbers` (`tuple[int]`): A tuple of integers.

#### `is_solvable(self) -> bool`

This method checks if the puzzle is solvable. It calculates the number of inversions in the start and goal states and uses this information to determine if the puzzle is solvable.

## Technical Concepts

The concept of inversions is used in this code to determine if a puzzle is solvable. An inversion is a pair of numbers where the number on the left is greater than the number on the right. The number of inversions in a puzzle is used to determine if it is solvable. If the width of the puzzle is even, then the puzzle is solvable if the number of inversions in the start state plus the row index of the blank square is even. If the width of the puzzle is odd, then the puzzle is solvable if the number of inversions in the start state is even.