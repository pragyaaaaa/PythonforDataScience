import pandas as pd

stats = pd.read_csv("..\\DataSets\\P4-Demographic-Data.csv")
# print(stats.to_string())
# print(stats.columns)
# print(stats.info())
# print(stats.head())
# print(stats.tail())
# print(stats.describe())
# print(stats.describe().transpose())

# Renaming columns of dataframe
# print(stats.columns)
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers',
                 'IncomeGroup']
# print(stats.columns)

# sub-setting dataframes in Pandas- by rows, columns and combining both
# slicing rows: by default
# print(stats[::-1].to_string())  # reversed
# slicing columns
# print(stats[['CountryName', 'BirthRate']].head())  # passing 'list' of columns we want to slice to dataframe
# print(stats.BirthRate)  # quick access to columns if column name is one word
# combining rows and column slicing
# print(stats[['CountryName', 'BirthRate']][4:19].to_string())

# add column to dataframe
stats['temp_column'] = stats.BirthRate * stats.InternetUsers
print(stats.temp_column.head())
print(stats.columns)

# removing a column
stats = stats.drop('temp_column',
                   axis=1)  # doesn't modify stats, creates a new object that's why we need to override our dataframe
print(stats.columns)
