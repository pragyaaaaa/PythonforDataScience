import matplotlib.pyplot as plt

from DataSets import BasketballDataSet as d

salary = d.Salary
seasons = d.Seasons
players = d.Players
players_dict = d.Pdict


def player_plot_salary(player_dict, color='Black', line_style=':', mark='s'):
    for name in player_dict:
        plt.plot(salary[player_dict[name]], c=color, ls=line_style, marker=mark, ms=7, label=players[player_dict[name]])
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xticks(list(range(0, 10)), seasons, rotation='vertical')
    plt.show()


player_plot_salary(players_dict, 'red', '--', 'o')
