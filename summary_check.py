import pandas as pd

# Load the dataset
df = pd.read_csv("data/WBBStatsFile01.csv")

# Check if any values in "Free Throws Made" contain commas
if df['Free Throws Made'].dtype == object:
    df['Free Throws Made'] = pd.to_numeric(df['Free Throws Made'].str.replace(',', ''), errors='coerce')

# Total number of teams
total_teams = df.shape[0]

# Team with highest Free Throw Percentage
top_ft_team = df.loc[df['Free Throw Percentage Season'].idxmax(), 'Team']

# Average games played
avg_games = df['Games'].mean()

# Team with highest Field Goal Percentage
top_fg_team = df.loc[df['FieldGoalPercentage'].idxmax(), ['Team', 'FieldGoalPercentage']]

# Team with the most wins
most_wins = df.loc[df['Wins'].idxmax(), ['Team', 'Wins']]

# Show the answers
print("🟢 Total Teams:", total_teams)
print("🏀 Team with Best FT%:", top_ft_team)
print("📊 Average Games Played:", round(avg_games, 2))
print("🥇 Best FG% Team:", top_fg_team['Team'], "-", top_fg_team['FieldGoalPercentage'])
print("🏆 Team with Most Wins:", most_wins['Team'], "-", most_wins['Wins'], "wins")