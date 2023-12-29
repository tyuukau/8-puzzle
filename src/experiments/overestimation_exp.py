import torch

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from ..utils import make_dir

from ..ml import get_model, batch_infer


def conduct_overestimation_experiment(
    input_file_path: str, experiment_folder_path: str, n: int = 0
) -> None:
    make_dir(experiment_folder_path)

    if n > 0:
        df = pd.read_csv(input_file_path, nrows=n)
    else:
        df = pd.read_csv(input_file_path)

    df = df.drop_duplicates()

    model = get_model()

    predicted_costs = batch_infer(df, model)
    df["predicted_cost"] = predicted_costs

    columns_to_use = [str(i) for i in range(16)]  # Create a list of column names '0' to '15'
    df.drop_duplicates(subset=columns_to_use, inplace=True)

    len(df)

    plt.rcParams["font.family"] = "SF Compact Text"
    font_scale = 2
    sns.set(font_scale=font_scale, font="SF Compact Text")

    df["ann_residual"] = df["predicted_cost"] - df["cost"]

    print("Creating residual plot for ANN distance")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="cost", y="ann_residual", alpha=0.7)
    plt.axhline(y=0, color="red", linestyle="--")
    plt.xlabel("Cost")
    plt.ylabel("Residuals")
    plt.tight_layout()
    plt.savefig(experiment_folder_path + "ann_residual_plot.png")

    over_df = df[df["ann_residual"] > 0]
    print("Overestimated instance percentage: ", len(over_df) / len(df))

    df.to_csv(experiment_folder_path + "experiment1_results.csv")
