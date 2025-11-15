import pandas as pd

def roi_score(row: pd.Series) -> float:
    """
    Calculate a simple ROI score for a certificate.
    Factors: issuer credibility, cost, duration, level.
    """
    credibility = 1.0 if any(x in row["issuer"] for x in ["Google", "Microsoft", "AWS", "IBM"]) else 0.7
    cost_bonus = {"Free": 1.0, "Low": 0.8, "Paid": 0.6}.get(row["cost"], 0.7)
    duration = row.get("duration_hours", 10)
    duration_penalty = max(0.4, 1.0 - (float(duration) / 200.0))
    level_weight = {"Beginner": 0.9, "Intermediate": 1.0, "Advanced": 1.1}.get(row["level"], 1.0)

    return round((credibility * 0.4 + cost_bonus * 0.3 + duration_penalty * 0.2) * level_weight, 3)

def add_scores(df: pd.DataFrame) -> pd.DataFrame:
    """Add ROI scores to the dataframe."""
    df = df.copy()
    df["roi_score"] = df.apply(roi_score, axis=1)
    return df