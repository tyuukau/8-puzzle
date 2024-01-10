from typing import List
import streamlit as st

import threading
import pandas as pd
import random

from src.algorithms.abstract_search import InformedSearchAlgorithm
from src.game import Game, ResultRecord
from src.game_config import GameConfig
from src.state import State
from src.algorithms import AStar, GBFS
from src.heuristics import manhattan_distance, ann_distance

df = pd.read_csv("data/input/experimental_data.csv")


def generate_random_board(df: pd.DataFrame = df) -> str:
    random_index = random.randint(0, len(df) - 1)
    random_row = df.iloc[random_index]

    concatenated_values = " ".join(str(random_row[str(i)]) for i in range(16))
    return concatenated_values


def parse_board_string(board_string: str) -> List[int]:
    board_list = list(map(int, board_string.split()))
    if not (set(board_list) == set(range(16)) and len(board_list) == 16):
        raise ValueError("Invalid board")
    if not _is_board_playable(board_list):
        raise ValueError("Unplayable board")
    return board_list


def _is_board_playable(board: List[int]) -> bool:
    game_config = GameConfig(
        start_state=State(*board),
        goal_state=State(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0),
    )
    return game_config.is_solvable()


def play_on_one(
    start_board: List[int], algorithm: InformedSearchAlgorithm, heuristic
) -> ResultRecord:
    game_config = GameConfig(
        start_state=State(*start_board),
        goal_state=State(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0),
    )
    algorithm_instance = algorithm(heuristic=heuristic)
    g = Game(game_config=game_config, algorithm=algorithm_instance, ignore_solvability=False)

    def run_game():
        nonlocal result_record
        result_record = g._play()

    result_record = None

    game_thread = threading.Thread(target=run_game)
    game_thread.start()

    # Set a timeout for the thread
    timeout_seconds = 60  # Adjust as needed
    game_thread.join(timeout_seconds)

    # Check if the thread is still running after the timeout
    if game_thread.is_alive():
        # If it's still running, terminate the thread and handle timeout
        game_thread.terminate()  # You may need to implement the termination logic
        result_record = None  # Handle the timeout situation

    return result_record


st.set_page_config(
    layout="wide",
    page_title="15-puzzle demo",
    page_icon="🤖",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .big-font {
        font-size:30px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("15-puzzle demo")

st.sidebar.markdown("### Board:")
board_choice = st.sidebar.text_input(
    "Type 16 integers from 0 to 15, order is random.\nExample: 12 0 15 2 8 4 3 5 6 14 1 11 10 7 9 13"
)

st.sidebar.markdown("### Algorithm:")
algo_list = ["A*", "GBFS"]
algo_choice = st.sidebar.selectbox("Choose one...", algo_list)

st.sidebar.markdown("### Heuristic:")
heu_list = ["Manhattan distance", "ANN distance"]
heu_choice = st.sidebar.selectbox("Choose one...", heu_list)

st.sidebar.markdown("### Let's Run!")
exec_btn = st.sidebar.button("Execute")

random_exec_btn = st.sidebar.button("Random board and execute")

if exec_btn:
    try:
        board = parse_board_string(board_choice)
    except Exception as e:
        st.error(
            f"Board is not valid or not playable. Please provide a valid board.\nError: {e}"
        )
        st.stop()

    heuristic = ann_distance if heu_choice == "ANN distance" else manhattan_distance
    algorithm = AStar if algo_choice == "A*" else GBFS

    result_record = play_on_one(start_board=board, algorithm=algorithm, heuristic=heuristic)
    st.write(result_record.time_cp)


if random_exec_btn:
    board_choice = generate_random_board()
    try:
        board = parse_board_string(board_choice)
    except Exception as e:
        st.error(
            f"Board is not valid or not playable. Please provide a valid board.\nError: {e}"
        )
        st.stop()

    heuristic = ann_distance if heu_choice == "ANN distance" else manhattan_distance
    algorithm = AStar if algo_choice == "A*" else GBFS

    result_record = play_on_one(start_board=board, algorithm=algorithm, heuristic=heuristic)
    st.write(result_record.time_cp)
