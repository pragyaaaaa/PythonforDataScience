import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

plt.rcParams['figure.figsize'] = 8, 4
warnings.filterwarnings('ignore')
stats = pd.read_csv("..\\DataSets\\P4-Demographic-Data.csv")
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers',
                 'IncomeGroup']
vis1 = sns.distplot(stats["InternetUsers"])
plt.show()
