#!/bin/python3

import math
import os
import random
import re
import sys
import collections
import itertools


# Complete the countTriplets function below.
def countTriplets(arr, r):
    powers = collections.defaultdict(list)
    power_counts = collections.defaultdict(int)
    triplets = 0
    for i, num in enumerate(arr):
        first, second, power = get_power_and_pairs(num, r)
        if power.is_integer():
            triplets += get_new_triplets_count(first, second, powers, power_counts)
            record_new_power(powers, power_counts, power, i)
    return triplets


def get_power_and_pairs(number, base):
    current_power = round(math.log(number, base), 2)
    return current_power - 2, current_power - 1, current_power


# def count_invalid_first_positions(first_positions, second_position):
#     first_positions_larger_than_second = itertools.takewhile(lambda x: x > second_position, iter(first_positions[::-1]))
#     return len(list(first_positions_larger_than_second))


def count_invalid_first_positions(first_positions, second_position):
    invalid = 0
    i = -1
    while True:
        try:
            n = first_positions[i]
        except IndexError:
            break
        if n > second_position:
            invalid += 1
            i -= 1
            continue
        break
    return invalid


def get_new_triplets_count(first, second, powers, power_counts):
    triplets = 0
    if first in powers and second in powers:
        # potential for triplets
        second_positions = powers[second]
        for s in second_positions:
            first_position_count = power_counts[first]
            first_positions_larger_than_second = count_invalid_first_positions(powers[first], s)
            triplets += first_position_count - first_positions_larger_than_second
    return triplets


def record_new_power(powers, power_counts, power, i):
    powers[power].append(i)
    power_counts[power] += 1
    return powers


if __name__ == '__main__':
    assert countTriplets([1, 5, 5, 25, 125], 5) == 4
