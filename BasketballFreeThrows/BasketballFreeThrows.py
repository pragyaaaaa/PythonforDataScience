# Analysing the trend of top 10 basketball players over 10 years
import numpy as np
from DataSets import BasketballDataSet as d
import matplotlib.pyplot as plt

salary = d.Salary
seasons = d.Seasons
players = d.Players
plt.plot(salary[0], c='Black', ls=':', marker='s', ms=7, label=players[0])
plt.plot(salary[1], c='Red', ls='-.', marker='o', ms=7, label=players[1])
plt.plot(salary[2], c='gold', ls='-', marker='v', ms=7, label=players[2])
plt.plot(salary[3], c='darkorchid', ls='--', marker='<', ms=7, label=players[3])
plt.plot(salary[4], c='teal', ls=':', marker='P', ms=7, label=players[4])
plt.plot(salary[5], c='cyan', ls='-.', marker='D', ms=7, label=players[5])
plt.plot(salary[6], c='crimson', ls='-', marker='X', ms=7, label=players[6])
plt.plot(salary[7], c='orchid', ls='--', marker='H', ms=7, label=players[7])
plt.plot(salary[8], c='green', ls=':', marker='8', ms=7, label=players[8])
plt.plot(salary[9], c='salmon', ls='-.', marker='>', ms=7, label=players[9])
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(list(range(0, 10)), seasons, rotation='vertical')
plt.show()
