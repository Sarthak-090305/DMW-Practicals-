import pandas as pd

file_path = r"C:\Users\sarth\OneDrive\Desktop\sem6\DMW\p2 DMW\NBA_2018-19_Season - NBA_2018-19_Season.csv"
df = pd.read_csv(file_path)

print("\nDataset Loaded Successfully\n")

# 1
print("1) Average Age:", df["Age"].mean())

# 2
print("\n2) Games played by each player:")
print(df[["Player", "Games"]])

# 3
print("\n3) Total Teams:", df["Team"].nunique())

# 4
print("\n4) Minimum Age:", df["Age"].min())

# 5
print("\n5) Maximum Age Player Details:")
print(df[df["Age"] == df["Age"].max()])

# 6
print("\n6) Total Games in Eastern Region:")
print(df[df["Conference"] == "Eastern"]["Games"].sum())

# 7
print("\n7) Total Regions:", df["Conference"].nunique())

# 8
print("\n8) Players from Boston Celtics:")
print(df[df["Team"] == "Boston Celtics"]["Player"])

# 9
print("\n9) Total Games in each Division:")
print(df.groupby("Division")["Games"].sum())

# 10
print("\n10) Player with Maximum Points:")
print(df.loc[df["Points"].idxmax()])

# 11
print("\n11) Player with Lowest Personal Fouls:")
print(df.loc[df["Personal Fouls"].idxmin()])

# 12
print("\n12) Player with Highest 3-Point Attempts:")
print(df.loc[df["3-Point Field Goal Attempts"].idxmax()]
      [["Player", "3-Point Field Goal Attempts", "3-Point Field Goal Percentage"]])

# 13
print("\n13) Average Points:", df["Points"].mean())

# 14
print("\n14) Average Age by Division:")
print(df.groupby("Division")["Age"].mean())

# 15
print("\n15) Total Fouls in each Team:")
print(df.groupby("Team")["Personal Fouls"].sum())
