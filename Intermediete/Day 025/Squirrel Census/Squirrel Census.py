import pandas as pd

# count squirrel based on color
df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250507.csv")
color = df["Primary Fur Color"].value_counts()
color.to_csv("color.csv")
print(color)