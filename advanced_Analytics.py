# advanced_analytics.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("D:\Masters ADS\Task_05_Descriptive_Stats\data\WBBStatsFile01.csv")

# Clean numeric columns if they contain commas
for col in ['Free Throws Made', 'Free Throw Attempts', 'Total Turnovers']:
    if df[col].dtype == object:
        df[col] = pd.to_numeric(df[col].str.replace(",", ""), errors="coerce")


# 1. Create advanced metrics

df['Win %'] = (df['Wins'] / df['Games']) * 100
df['FT Made/Game'] = df['Free Throws Made'] / df['Games']
df['Turnovers/Game'] = df['Total Turnovers'] / df['Games']
df['FT%'] = df['Free Throws Made'] / df['Free Throw Attempts'] * 100
df['Efficiency Score'] = df['Wins'] + df['FieldGoalPercentage'] + df['FT%']


# 2. Print key advanced insights

print("🏆 Top 5 Teams by Win %:")
print(df[['Team', 'Win %']].sort_values('Win %', ascending=False).head(5))

print("\n❌ Lowest 5 Assist-to-Turnover Ratio:")
print(df[['Team', 'AssistTurnoverRatio']].sort_values('AssistTurnoverRatio').head(5))

print("\n🎯 Top 5 FT Made per Game:")
print(df[['Team', 'FT Made/Game']].sort_values('FT Made/Game', ascending=False).head(5))

print("\n🔥 Top 5 Teams by Field Goal %:")
print(df[['Team', 'FieldGoalPercentage']].sort_values('FieldGoalPercentage', ascending=False).head(5))

print("\n🔻 Teams with Most Turnovers per Game:")
print(df[['Team', 'Turnovers/Game']].sort_values('Turnovers/Game', ascending=False).head(5))

print("\n🌟 Top 5 Efficient Teams (Wins + FG% + FT%):")
print(df[['Team', 'Efficiency Score']].sort_values('Efficiency Score', ascending=False).head(5))


# 3. Correlation matrix of predictors

corr_cols = ['Win %', 'AssistPerGame', 'AssistTurnoverRatio', 'FT%', 'FieldGoalPercentage', 'Turnovers/Game']
plt.figure(figsize=(10, 6))
sns.heatmap(df[corr_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix – Predictors of Team Success")
plt.tight_layout()
plt.savefig("D:\Masters ADS\Task_05_Descriptive_Stats/figures/advanced_correlation_heatmap.png")
plt.show()


# 4. FT% vs Win % (Scatterplot)

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='FT%', y='Win %')
plt.title("Free Throw % vs Win %")
plt.xlabel("FT%")
plt.ylabel("Win %")
plt.tight_layout()
plt.savefig("D:\Masters ADS\Task_05_Descriptive_Stats/figures/ft_vs_win_percent.png")
plt.show()


# 5. Assist Per Game vs Win % (Scatterplot)

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='AssistPerGame', y='Win %')
plt.title("Assist Per Game vs Win %")
plt.xlabel("Assist Per Game")
plt.ylabel("Win %")
plt.tight_layout()
plt.savefig("D:\Masters ADS\Task_05_Descriptive_Stats/figures/assist_vs_win_percent.png")
plt.show()
