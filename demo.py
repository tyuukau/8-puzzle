import streamlit as st

import threading
import time
import pandas as pd
import random

from src.algorithms.abstract_search import InformedSearchAlgorithm
from src.game import Game, ResultRecord, TimeoutError
from src.game_config import GameConfig
from src.node import Node
from src.state import State
from src.algorithms import AStar, GBFS
from src.heuristics import CallableHeuristicClass, manhattan_distance, ann_distance

df = pd.read_csv("data/input/experimental_data.csv")

NUM_15_PUZZLE = 16


def generate_random_board(df: pd.DataFrame = df) -> str:
    random_index = random.randint(0, len(df) - 1)
    random_row = df.iloc[random_index]

    concatenated_values = " ".join(str(random_row[str(i)]) for i in range(NUM_15_PUZZLE))
    return concatenated_values


def parse_board_string(board_string: str) -> list[int]:
    board_list = list(map(int, board_string.split()))
    if not (set(board_list) == set(range(NUM_15_PUZZLE)) and len(board_list) == NUM_15_PUZZLE):
        raise ValueError("Invalid board")
    if not _is_board_playable(board_list):
        raise ValueError("Unplayable board")
    return board_list


def _is_board_playable(board: list[int]) -> bool:
    game_config = GameConfig(
        start_state=State(*board),
    )
    return game_config.is_solvable()


def play_on_one(
    start_board: list[int],
    algorithm: InformedSearchAlgorithm,
    heuristic: CallableHeuristicClass,
    timeout: int = 10,
) -> ResultRecord:
    game_config = GameConfig(
        start_state=State(*start_board),
    )
    algorithm_instance = algorithm(heuristic=heuristic)
    g = Game(game_config=game_config, algorithm=algorithm_instance, ignore_solvability=False)

    heu_choice = "ANN distance" if heuristic == ann_distance else "Manhattan distance"
    algo_choice = algorithm_instance.name

    st.write(f"Gameplay: {algo_choice} algorithm and {heu_choice} heuristic.")

    def run_play():
        nonlocal search_result
        try:
            search_result = g._play()
        except TimeoutError:
            search_result = None

    search_result = None

    start_time = time.time()

    play_thread = threading.Thread(target=run_play)
    play_thread.start()
    play_thread.join(timeout=timeout)

    if play_thread.is_alive():
        st.write("Time limit reached. Game aborted...")
        st.stop()

    end_time = time.time()
    execution_time = end_time - start_time

    path = search_result.path
    path_length = len(search_result.path) - 1
    time_cp = search_result.time_cp
    space_cp = search_result.space_cp

    return ResultRecord(path, path_length, time_cp, space_cp, execution_time)


def display_node_state(node: Node | list[int]) -> None:
    try:
        n = int(len(node.state.array) ** 0.5)
        array = node.state.array
    except Exception:
        n = int(len(node) ** 0.5)
        array = node

    columns = st.columns(n)
    for i in range(n):
        for j in range(n):
            idx = i * n + j
            columns[j].write(array[idx])


def main(board_choice, heu_choice, algo_choice, time_choice) -> None:
    try:
        board = parse_board_string(board_choice)
    except Exception as e:
        st.error(
            f"Board is not valid or not playable. Please provide a valid board.\nError: {e}"
        )
        st.stop()

    heuristic = ann_distance if heu_choice == "ANN distance" else manhattan_distance
    algorithm = AStar if algo_choice == "A*" else GBFS
    timeout = time_choice

    result_record = play_on_one(
        start_board=board, algorithm=algorithm, heuristic=heuristic, timeout=timeout
    )

    path = result_record.path

    if path:
        st.write("### Basic information")
        st.write("Board:")
        display_node_state(board)
        st.write(f"Path length: {result_record.path_length}")
        st.write(f"Time complexity: {result_record.time_cp}")
        st.write(f"Space complexity: {result_record.space_cp}")
        st.write(f"Runtime: {result_record.time}")

        st.write("### Path")
        for idx, node in enumerate(path):
            if idx == 0:
                st.write("Start node:")
            else:
                st.write(f"Node {idx}:")
            display_node_state(node.state.array)
            st.write("---")

        # if st.button("Next Node"):
        #     if current_node_idx < len(path) - 1:
        #         current_node_idx += 1
        #     else:
        #         st.write("End of Path reached.")
        #     st.write(f"Next Node: {current_node_idx + 1}")
        #     display_node_state(path[current_node_idx])
    else:
        st.write("No path found within time limit.")


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

st.sidebar.markdown("### Timeout:")
options = [10, 20, 30, 40, 50, 60]
time_choice = st.sidebar.selectbox("Choose one... (seconds)", options)

st.sidebar.markdown("### Let's Run!")
exec_btn = st.sidebar.button("Execute")

random_exec_btn = st.sidebar.button("Random board and execute")

if exec_btn:
    main(board_choice, heu_choice, algo_choice, time_choice)

if random_exec_btn:
    board_choice = generate_random_board()
    main(board_choice, heu_choice, algo_choice, time_choice)
