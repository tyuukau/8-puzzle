from state import State


def mistile_distance(current_state: State, goal_state: State) -> int:
    """
    Calculates the misplaced-tile distance between the current state and the goal state.

    Args:
    - `current_state` (`State`): The current state of the puzzle.
    - `goal_state` (`State`): The goal state of the puzzle.

    Returns:
    - `int`: The Manhattan distance between the current state and the goal state.
    """
    return sum(c1 != c2 for c1, c2 in zip(current_state.array, goal_state.array))


def manhattan_distance(current_state: State, goal_state: State) -> int:
    """
    Calculates the Manhattan distance between the current state and the goal state.

    Args:
    - `current_state` (`State`): The current state of the puzzle.
    - `goal_state` (`State`): The goal state of the puzzle.

    Returns:
    - `int`: The Manhattan distance between the current state and the goal state.
    """
    goal_pos = {
        val: goal_state.idx_to_pos(idx) for idx, val in enumerate(goal_state.array) if val != 0
    }

    sum = 0
    for idx, val in enumerate(current_state.array):
        if val != 0:
            current_i, current_j = current_state.idx_to_pos(idx)
            goal_i, goal_j = goal_pos[val]
            sum += abs(current_i - goal_i) + abs(current_j - goal_j)
    return sum


def gaschnig_distance(current_state: State, goal_state: State) -> int:
    """
    Calculates the Gaschnig distance between the current state and the goal state.

    Args:
    - `current_state` (`State`): The current state of the puzzle.
    - `goal_state` (`State`): The goal state of the puzzle.

    Returns:
    - `int`: The Manhattan distance between the current state and the goal state.

    See here: https://cse-robotics.engr.tamu.edu/dshell/cs625/gaschnig-note.pdf.
    """
    start = list(current_state.array)
    goal = list(goal_state.array)
    move = 0
    while start != goal:
        blank_index = start.index(0)
        if goal[blank_index] != 0:
            mismatch_index = start.index(goal[blank_index])
            start[blank_index] = goal[blank_index]
            start[mismatch_index] = 0
            move += 1
        else:  # blank in goal position
            for i in range(len(start)):
                if start[i] != goal[i]:
                    start[blank_index] = start[i]
                    start[i] = 0
                    move += 1
                    break
    return move


def main():
    a = State((1, 2, 3, 4, 0, 6, 7, 5, 8))
    b = State((1, 2, 3, 4, 5, 6, 7, 8, 0))
    print(mistile_distance(a, b))
    print(manhattan_distance(a, b))
    print(gaschnig_distance(a, b))


if __name__ == "__main__":
    main()
