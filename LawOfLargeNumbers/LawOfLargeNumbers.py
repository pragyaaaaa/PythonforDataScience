# The law of large numbers, in probability and statistics, states that as a sample size grows, it's mean gets closer
# to the average of the whole population.
import numpy as np
from numpy.random import randn

n = int(input("How many numbers you want to generate?:\t"))
counter = 0
for i in randn(n):
    if -1 < i < 1:
        counter += 1
hit_ratio = counter / n
hit_ratio_per=hit_ratio*100
print(f"{hit_ratio} i.e. {hit_ratio_per}% numbers fall between -1 and 1 for {n}.")
