# Machine Learning Module Documentation

This documentation provides an overview of the Machine Learning (ML) module in our system. The ML module is responsible for defining, training, and using machine learning models to solve puzzles. The module is implemented in Python and uses the PyTorch library for model definition, training, and inference.

## Table of Contents

1. [__init__.py](#__init__.py)
2. [inferring.py](#inferring.py)
3. [modelling.py](#modelling.py)
4. [Repository Link](#Repository-Link)

## __init__.py

[__init__.py](src/ml/__init__.py) is a file in the ML module. It is responsible for initializing the module and making it a package. This allows the module's classes and functions to be imported into other parts of the system.

## inferring.py

[inferring.py](src/ml/inferring.py) is a Python script in the ML module. It uses PyTorch to define and use a neural network model for solving puzzles. The script contains a class definition for the model, as well as functions for loading the model, making single inferences, and making batch inferences.

### PuzzleHeuristicModel Class

The PuzzleHeuristicModel class is defined in this script. It represents the neural network model used for solving puzzles.

## modelling.py

[modelling.py](src/ml/modelling.py) is a Python file in the ML module. It contains the implementation of a machine learning model for solving puzzles. The file includes the definition of a custom PyTorch Dataset class, a PyTorch Model class, and a training function. The code uses PyTorch for model definition, training, and inference, and pandas for data manipulation.

### PuzzleDataset Class

The PuzzleDataset class is defined in this file. It represents the dataset used for training the puzzle-solving model.

## Repository Link

You can find the ML module in our repository at the following link: [/src/ml](/src/ml).