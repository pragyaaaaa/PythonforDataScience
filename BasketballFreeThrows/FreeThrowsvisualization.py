import matplotlib.pyplot as plt
import numpy as np
from DataSets import BasketballDataSet as d

np.seterr(divide='ignore',
          invalid='ignore')  # to ignore the runtime time warning for dividing by 0 in playing_style array

# freethrow attempts per game
# accuracy of free throws
# palying-style: (Points-freethrows)/fieldgoals

games = d.Games
free_throws = d.Free_Throws
free_throw_attempts = d.Free_Throw_Attempts
points = d.Points
field_goals = d.FieldGoals
seasons = d.Seasons
players_dict = d.Pdict
playing_style = (points - free_throws) / field_goals
players = d.Players


def player_plot(data_matrix=free_throw_attempts, player_dict=players_dict):
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
player_plot(free_throws, players_dict)
player_plot(playing_style, players_dict)
