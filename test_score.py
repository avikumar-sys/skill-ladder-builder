from skill_ladder.fetch import load_certificates
from skill_ladder.score import add_scores

# Load dataset
df = load_certificates()

# Add ROI scores
scored = add_scores(df)

# Print first few rows with scores
print(scored.head())