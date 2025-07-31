# Research Task 05 – LLM Reasoning with NCAA Basketball Data

## 👩‍💻 Objective
To evaluate how well a large language model (ChatGPT) can answer questions about structured sports data, by comparing its answers to Python-calculated ground truth.

## 🗃️ Dataset
- 349 rows × 28 columns
- 2023–2024 NCAA Women’s Basketball Season
- Includes: Wins, Losses, FT%, FG%, Assists, Blocks, Turnovers, etc.

## 🧪 Testing Approach
1. Ask ChatGPT to compute total, average, max values from CSV data
2. Cross-check answers using Python
3. Record any mismatches or hallucinations

## ✅ Results Summary
- For all 5 basic stats, ChatGPT matched Python's output exactly.
- LLMs are effective for basic arithmetic/ranking with well-formatted CSVs.

