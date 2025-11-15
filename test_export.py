from pathlib import Path
from skill_ladder.fetch import load_certificates
from skill_ladder.score import add_scores
from skill_ladder.map import sequence_ladder
from skill_ladder.export import plot_ladder

# Load dataset
df = load_certificates()

# Add ROI scores
scored = add_scores(df)

# Sequence into ladder
ladder = sequence_ladder(scored)

# Export visualization
out_path = Path("docs") / "ladder_demo.png"
plot_ladder(ladder, out_path)

print(f"Ladder visualization saved to {out_path}")