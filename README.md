# 🚀 Skill Ladder Builder
**Turn confusing certificate choices into clear career roadmaps.**

Learners worldwide waste money and months of effort on certificates that don’t advance their careers.  
Skill Ladder Builder scores certifications on **ROI (issuer credibility, cost, duration, level)** and sequences them into structured ladders: **Beginner → Intermediate → Advanced**.  
The result: transparent, data‑driven career paths you can act on today.

---

## ✨ Why it matters
- **Real pain point:** Learners struggle to compare certificates and end up stacking low‑impact ones.
- **Direct fix:** Transparent ROI scoring and reproducible ladders remove guesswork.
- **Outcome:** Faster skill growth, lower costs, and clearer paths to target roles.

---

## 💡 Why we’re different
- **ROI scoring engine:** Not just a list—each certificate is ranked on tangible value.
- **Ladder sequencing:** Clear progression from fundamentals to advanced credentials.
- **Reproducibility:** Modular pipeline you can audit, extend, and benchmark.
- **Actionability:** Visuals and tables make choices obvious, not opinion‑based.

---

## 🏆 Impact example
- **Goal:** AI Engineer (entry → mid)
- **Result:** Skip low‑ROI certificates; follow a ladder with higher issuer credibility and better skill coverage.
- **Benefit:** Save money and months of effort while building a coherent skill stack.

---

## 🎥 Demo
- **Short video:** Add a 2–3 minute demo link here (Loom/YouTube).
- **Quick flow:** Input goal → generate ladder → explore ROI chart → export roadmap.

> Tip: Keep the demo under 3 minutes. Show the transformation (confusion → clarity), not every button.

---

## 🔍 Features
- **Data loader (`fetch.py`):** Imports certificate datasets.
- **Scoring engine (`score.py`):** Calculates ROI from issuer, cost, duration, and level.
- **Ladder sequencer (`map.py`):** Orders certificates into a coherent path.
- **Visualization (`export.py`):** Scatter plots and tables for ROI vs. ladder step.
- **Streamlit UI (`app/streamlit_app.py`):** Interactive interface for live demos.

---

## ⚙️ Getting started

### Prerequisites
- **Python:** 3.11+
- **Package manager:** pip

### Installation
```bash
git clone https://github.com/avikumar-sys/skill-ladder-builder.git
cd skill-ladder-builder
pip install -r requirements.txt
