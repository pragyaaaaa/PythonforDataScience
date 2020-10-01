import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

plt.rcParams['figure.figsize'] = 8, 4
warnings.filterwarnings('ignore')
stats = pd.read_csv("..\\DataSets\\P4-Demographic-Data.csv")
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers',
                 'IncomeGroup']
# xaxis = input("Enter x axis: \t")
# yaxis = input("Enter y-axis: \t")
# vis1 = sns.boxplot(data=stats, x=xaxis, y=yaxis)
vis = sns.lmplot(data=stats, x="InternetUsers", y='BirthRate', fit_reg=False, hue="IncomeGroup", size=5,
                 scatter_kws={"s": 200})
plt.show()
