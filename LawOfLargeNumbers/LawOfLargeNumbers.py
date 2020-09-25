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
    # print(f"{hit_ratio} i.e. {hit_ratio_per}% numbers fall between -1 and 1 for {num}.")
    return hit_ratio_per


def input_for_lln():
    n = int(input("How many numbers you want to generate?:\t"))
    law_of_large_numbers(n)
    return n


def compare_for_inputs(input_1, input_2):
    h_r_ip1 = law_of_large_numbers(input_1)
    h_r_ip2 = law_of_large_numbers(input_2)
    print(f"For {input_1}, {h_r_ip1}% numbers fit criteria, where as for {input_2}, {h_r_ip2}% numbers do.")


in_1 = input_for_lln()
in_2 = input_for_lln()
compare_for_inputs(in_1, in_2)
