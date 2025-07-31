# Research Task 05 – Prompt Testing Log

## ✅ Objective
Test how well a large language model (ChatGPT) can answer basic statistical questions using a raw CSV dataset (NCAA Women’s Basketball 2023–24).

## 🗃️ Dataset Info
- 349 teams
- Columns: Wins, Losses, Free Throw %, FG%, Assists, Turnovers, etc.

---

## 🧪 Prompt 1 – Basic Stats from Full Dataset

### Prompted Questions
1. How many teams are listed?
2. Which team had the highest Free Throw Percentage?
3. What is the average number of games played?
4. Which team had the highest Field Goal Percentage?
5. Which team had the most wins?

### Python Output (Ground Truth)
- Teams: 349
- Best FT%: Creighton – 82.7
- Avg Games: 31.87
- Best FG%: Indiana – 50.4
- Most Wins: South Carolina – 38

### ChatGPT Answers
- Teams: 349 ✅
- Best FT%: Creighton ✅
- Avg Games: 31.87 ✅
- Best FG%: Indiana ✅
- Most Wins: South Carolina ✅

### Notes
✅ LLM was completely accurate for this prompt.

