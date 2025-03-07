# node.py

This Python file defines two classes, `Node` and `PNode`, which represent nodes in a search tree. These nodes are used in search algorithms, such as A* and BFS, to represent the state of a problem at a given point, the action taken to reach this state, the cost of the path from the initial state to this state, and the parent node that this state was expanded from.

## Class: Node

The `Node` class is a basic representation of a node in a search tree. It has four attributes: `state`, `parent`, `action`, and `cost`.

### Attributes

- `state` (`State`): The state of the node. This is an instance of the `State` class, which represents the state of the problem that this node represents.
- `parent` (`Node`): The parent node of this node. This is the node from which this node was expanded.
- `action` (`Action`): The action taken to reach this node from its parent node. This is an instance of the `Action` enum, which can be `UP`, `DOWN`, `LEFT`, or `RIGHT`.
- `cost` (`int`): The cost of the path from the initial state to this node. This is the sum of the costs of the actions taken to reach this node from the initial state.

### Methods

- `expand() -> list[Node]`: This method returns a list of nodes that can be reached from this node by taking one action. It does this by iterating over all possible actions, applying each action to the current state to get a new state, and creating a new node for each reachable state.

## Class: PNode

The `PNode` class is a subclass of `Node` that adds an additional attribute, `f_cost`. This class is used in search algorithms that use a heuristic function to estimate the cost of the path from the initial state to the goal state.

### Attributes

- `f_cost` (`int`): The f-cost of the node. This is the sum of the cost of the path from the initial state to this node and the heuristic estimate of the cost of the path from this node to the goal state.

### Methods

- `expand() -> list[PNode]`: This method works in the same way as the `expand` method of the `Node` class, but it returns a list of `PNode` instances instead of `Node` instances.

## Enum: Action

The `Action` enum represents the actions that can be taken to move from one state to another. It has four values: `UP`, `DOWN`, `LEFT`, and `RIGHT`.

## Usage

Here is an example of how to use these classes:

```python
from node import Node, Action, State

# Create an initial state
initial_state = State()

# Create the initial node
initial_node = Node(state=initial_state, parent=None, action=None, cost=0)

# Expand the initial node
neighbors = initial_node.expand()

# Print the state of each neighbor
for neighbor in neighbors:
    print(neighbor.state)
```

This will print the state of each node that can be reached from the initial state by taking one action.