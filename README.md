# Research Task 05 – LLM Reasoning with NCAA Basketball Data

## 👩‍💻 Objective
Evaluate how well a large language model (ChatGPT) can analyze structured data (CSV) and answer analytical questions by comparing its answers with verified Python outputs. In this task, we focused on NCAA Women’s Basketball team stats from the 2023–2024 season.

---

## 🗃️ Dataset Overview
- 📊 349 teams × 28 columns (1 row per team)
- 🏀 NCAA Women's Basketball (2023–2024)
- 📁 Columns include: Wins, Losses, Free Throw %, Field Goal %, Assists, Turnovers, Blocks, etc.
- ❗ The raw dataset (`WBBStatsFile01.csv`) is excluded from the GitHub repo (see `.gitignore`).

---

## 🧪 Testing Approach

### ✅ Basic Phase
1. Extracted total teams, top FT%, avg games, and FG% in Python.
2. Asked ChatGPT the same questions using the full CSV data.
3. Compared results — 100% match for simple statistical questions.

### 🔍 Advanced Phase
1. Engineered new metrics in Python:
   - Win %
   - FT Made per Game
   - Turnovers per Game
   - FT%
   - Composite Efficiency Score = Wins + FG% + FT%
2. Visualized insights via scatterplots and heatmaps.
3. Asked ChatGPT advanced ranking & reasoning questions using engineered metrics.
4. Evaluated LLM’s ability to identify correlations and predictors.

---

## ✅ Results Summary

| Insight | ChatGPT | Python | Match? |
|--------|---------|--------|--------|
| Total Teams | ✅ 349 | ✅ 349 | ✅ |
| Top FT% Team | ✅ Creighton | ✅ Creighton | ✅ |
| Best FG% Team | ✅ Indiana | ✅ Indiana | ✅ |
| Top Win % | ✅ South Carolina | ✅ South Carolina | ✅ |
| Most Turnovers/Game | ✅ Alabama St. | ✅ Alabama St. | ✅ |
| Efficient Team (Custom Score) | ✅ Iowa | ✅ Iowa | ✅ |

- LLM accurately handled both basic and engineered-stat queries.
- Correlation findings (e.g., FG% ↔ Win%) matched Python visual analysis.
- LLM showed good reasoning when asked to rank or infer based on combined metrics.

---

## 📈 Visual Outputs (in `/figures`)
- `advanced_correlation_heatmap.png`
- `ft_vs_win_percent.png`
- `assist_vs_win_percent.png`

---

## 🔍 Key Takeaways
- ChatGPT can reliably reason over well-structured numeric data.
- Engineered metrics and visual analysis enhanced insight depth.
- Win % is best predicted by a combination of FG%, FT%, and Assists.
- High Turnovers correlate negatively with success.





