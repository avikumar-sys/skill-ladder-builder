import pandas as pd

# Define order for levels
LEVEL_ORDER = {"Beginner": 1, "Intermediate": 2, "Advanced": 3}

def sequence_ladder(df: pd.DataFrame) -> pd.DataFrame:
    """
    Order certificates into a ladder by level and ROI score.
    """
    df = df.copy()
    df["level_rank"] = df["level"].map(LEVEL_ORDER).fillna(99)
    df.sort_values(by=["level_rank", "roi_score"], ascending=[True, False], inplace=True)
    df["step"] = range(1, len(df) + 1)

    cols = ["step", "domain", "level", "certificate", "issuer", "roi_score", "cost", "duration_hours", "tags"]
    return df[[c for c in cols if c in df.columns]]

def as_json_records(df: pd.DataFrame) -> list:
    """Convert ladder dataframe to JSON records."""
    return df.to_dict(orient="records")