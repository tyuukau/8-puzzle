# state.py

## Overview
The `state.py` file contains a single class, `State`, which represents a state of the 8-puzzle game. The 8-puzzle game is a sliding puzzle that consists of a frame of numbered square tiles in random order with one tile missing. The object of the puzzle is to place the tiles in order by making sliding moves that use the empty space.

## Class: State

### Description
The `State` class represents a state of the 8-puzzle game. It includes attributes to represent the width of the puzzle board, the flattened representation of the puzzle board, and the index of the blank tile in the puzzle board. It also includes methods to swap the positions of two tiles, get the position of the blank tile, and get the positions of all tiles.

### Attributes
- `width (int)`: The width of the puzzle board.
- `array (tuple[int])`: The flattened representation of the puzzle board.
- `blank (int)`: The index of the blank tile (0) in the puzzle board.

### Methods

#### `swap(self, i_old: int, j_old: int, i_new: int, j_new: int) -> State`
Swaps the positions of two tiles in the puzzle board and returns a new `State` object. The parameters are:
- `i_old, j_old`: The row and column indices of the tile to be moved.
- `i_new, j_new`: The row and column indices of the new position for the tile.

#### `get_blank_tile(self) -> tuple[int, int]`
Returns the (row, col) tuple of the blank tile in the puzzle board.

#### `get_positions(self) -> dict[int, tuple[int, int]]`
Returns a dictionary (tile, position) in the puzzle board.

### Example Usage
```python
# Create a new state
state = State(1, 2, 3, 4, 5, 6, 7, 8, 0)

# Swap the positions of two tiles
new_state = state.swap(2, 2, 2, 1)

# Get the position of the blank tile
blank_tile_position = state.get_blank_tile()

# Get the positions of all tiles
positions = state.get_positions()
```

### Technical Concepts
The `State` class uses the concept of a flattened representation of the puzzle board. This means that the 2D puzzle board is represented as a 1D tuple of integers. The position of a tile in the tuple corresponds to its position on the puzzle board. The blank tile is represented by the number 0.

The class also uses the concept of a width, which is the number of tiles in one row or column of the puzzle board. The width is calculated as the square root of the length of the array attribute.

The class uses the `math.isqrt` function to calculate the width. This function returns the integer square root of a number. For example, `math.isqrt(9)` returns `3`.

The class uses the `__slots__` mechanism to improve memory efficiency. The `__slots__` attribute is a list that contains the names of the attributes of the class. By defining `__slots__`, Python will not create a dictionary for each instance of the class, which saves memory.