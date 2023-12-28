import argparse

from src.preprocessing import evaluate_heuristics_on_dataset
from src.algorithms import AStar
from src.state import State
from src.game_config import GameConfig
from src.game import Game
from src.heuristics import manhattan_distance


def main():
    parser = argparse.ArgumentParser(description="Run game or evaluate heuristics.")

    parser.add_argument(
        "--input_file_path",
        type=str,
        default="data/input/fifteen-puzzle-6M.csv",
        help="Path to the input file.",
    )
    parser.add_argument(
        "--n",
        type=int,
        default=0,
        help="If n = 0, load all data, if n > 0, load n first rows from data.",
    )

    parser.add_argument(
        "--eda_folder_path",
        type=str,
        default="data/preprocess/",
        help="Path to the EDA folder.",
    )
    parser.add_argument(
        "--evaluate_heuristics_on_dataset",
        action="store_true",
        help="Flag to evaluate heuristics on the dataset.",
    )

    args = parser.parse_args()

    if args.evaluate_heuristics_on_dataset:
        evaluate_heuristics_on_dataset(
            input_file_path=args.input_file_path,
            evaluated_folder_path=args.eda_folder_path,
            n=args.n,
        )

    game_config = GameConfig(
        start_state=State(8, 6, 7, 2, 5, 4, 3, 0, 1),
        goal_state=State(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0),
    )
    algorithm = AStar(heuristic=manhattan_distance)
    g = Game(game_config=game_config, algorithm=algorithm, ignore_solvability=True)
    g.play()


if __name__ == "__main__":
    main()
