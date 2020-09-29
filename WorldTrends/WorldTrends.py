import pandas as pd

stats = pd.read_csv("..\\DataSets\\P4-Demographic-Data.csv")
print(stats.to_string())
print(stats.columns)