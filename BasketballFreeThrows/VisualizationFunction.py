import matplotlib.pyplot as plt

from DataSets import BasketballDataSet as d

salary = d.Salary
seasons = d.Seasons
players = d.Players
games = d.Games
players_dict = d.Pdict


def player_plot(data_matrix=salary, player_dict=players_dict):
    color = {"KobeBryant": 'Red', "JoeJohnson": "gold", "LeBronJames": "darkorchid", "CarmeloAnthony": "teal",
             "DwightHoward": "cyan", "ChrisBosh": "crimson",
             "ChrisPaul": "orchid", "KevinDurant": "green", "DerrickRose": "salmon", "DwayneWade": "black"}
    line_style = {"KobeBryant": ":", "JoeJohnson": "-.", "LeBronJames": "-", "CarmeloAnthony": "--",
                  "DwightHoward": ":", "ChrisBosh": "-.",
                  "ChrisPaul": "-", "KevinDurant": "--", "DerrickRose": ":", "DwayneWade": "-."}
    mark = {"KobeBryant": "o", "JoeJohnson": "v", "LeBronJames": "<", "CarmeloAnthony": "P", "DwightHoward": "D",
            "ChrisBosh": "X",
            "ChrisPaul": "H", "KevinDurant": "8", "DerrickRose": ">", "DwayneWade": "s"}
    for name in player_dict:
        plt.plot(data_matrix[player_dict[name]], c=color[name], ls=line_style[name], marker=mark[name], ms=7,
                 label=players[player_dict[name]])
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xticks(list(range(0, 10)), seasons, rotation='vertical')
    plt.show()


player_plot(games, players_dict)
player_plot(salary, players_dict)
