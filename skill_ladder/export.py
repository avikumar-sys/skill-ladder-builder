import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def plot_ladder(df: pd.DataFrame, out_path: Path):
    """
    Create a scatter plot of the ladder by step and ROI score.
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    # Color by level
    colors = {"Beginner": "#5cb85c", "Intermediate": "#f0ad4e", "Advanced": "#d9534f"}
    for level, group in df.groupby("level"):
        ax.scatter(group["step"], group["roi_score"], label=level, c=colors.get(level, "gray"))

    ax.set_xlabel("Step")
    ax.set_ylabel("ROI Score")
    ax.set_title("Career Ladder Visualization")
    ax.legend()

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(out_path)
    plt.close(fig)