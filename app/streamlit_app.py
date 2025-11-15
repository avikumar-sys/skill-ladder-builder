import streamlit as st
from skill_ladder.fetch import load_certificates
from skill_ladder.score import add_scores
from skill_ladder.map import sequence_ladder
from skill_ladder.export import plot_ladder
from pathlib import Path

st.title("📈 Skill Ladder Builder")

# Load and process data
df = load_certificates()
scored = add_scores(df)
ladder = sequence_ladder(scored)

# Show table
st.subheader("Certificate Ladder")
st.dataframe(ladder)

# Plot visualization
out_path = Path("docs") / "ladder_streamlit.png"
plot_ladder(ladder, out_path)
st.image(str(out_path))