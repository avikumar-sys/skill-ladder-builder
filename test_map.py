from skill_ladder.fetch import load_certificates
from skill_ladder.score import add_scores
from skill_ladder.map import sequence_ladder

# Load dataset
df = load_certificates()

# Add ROI scores
scored = add_scores(df)

# Sequence into ladder
ladder = sequence_ladder(scored)

# Print the ordered ladder
print(ladder)