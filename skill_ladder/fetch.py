import pandas as pd
from pathlib import Path

# Path to your dataset
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "certificates_master.csv"

def load_certificates() -> pd.DataFrame:
    """Load the master certificates dataset."""
    df = pd.read_csv(DATA_PATH)
    return df