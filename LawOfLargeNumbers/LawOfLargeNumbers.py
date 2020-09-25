# The law of large numbers, in probability and statistics, states that as a sample size grows, it's mean gets closer
# to the average of the whole population.
import numpy as np
from numpy.random import randn


def law_of_large_numbers(num):
    counter = 0
    for i in randn(num):
        if -1 < i < 1:
            counter += 1
    hit_ratio = counter / num
    hit_ratio_per = hit_ratio * 100
    print(f"{hit_ratio} i.e. {hit_ratio_per}% numbers fall between -1 and 1 for {num}.")


n = int(input("How many numbers you want to generate?:\t"))
law_of_large_numbers(n)
