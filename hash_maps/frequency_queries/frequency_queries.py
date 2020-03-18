#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
# 1 x: Insert x in your data structure.
# 2 y: Delete one occurence of y from your data structure, if present.
# 3 z: Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.

# For example, you are given array 
# The results of each operation are:
# queries = [(1,2), (2,2), (3,2), (1,1), (1,1), (2,1), (3,2)]
# Operation   Array   Output
# (1,1)       [1]
# (2,2)       [1]
# (3,2)                   0
# (1,1)       [1,1]
# (1,1)       [1,1,1]
# (2,1)       [1,1]
# (3,2)                   1

# Return an array with the output:
# [0, 1]
def freqQuery(queries):
    peak_frequency = 0  # so we can short circuit in operation 3
    frequencies = {}
    frequencies_keyed = {}
    output = []
    for q in queries:
        operation = q[0]
        value = q[1]
        if operation == 1:
            # 1 x: Insert x in your data structure.
            # peak_frequency = update_values_frequency(peak_frequency, frequencies, value, 1)
            peak_frequency = update_values_freq(peak_frequency, frequencies, value, 1, frequencies_keyed)
        elif operation == 2:
            # 2 y: Delete one occurence of y from your data structure, if present.
            peak_frequency = update_values_freq(peak_frequency, frequencies, value, -1, frequencies_keyed)
        else:
            # 3 z: Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.
            append_output_based_on_frequency(value, output, frequencies_keyed)
    return output


def append_output_based_on_frequency(query_frequency, output, frequencies_keyed):
    output.append(1 if query_frequency in frequencies_keyed else 0)


def update_values_freq(peak_frequency, frequencies, value, delta, frequencies_keyed):
    current_frequency = frequencies.get(value, 0)
    new_frequency = current_frequency + delta
    new_frequency = 0 if new_frequency < 0 else new_frequency

    frequencies[value] = new_frequency

    # remove value from old key in frequencies_keyed, its frequency changed
    if current_frequency > 0:
        frequencies_keyed[current_frequency].remove(value)
        if len(frequencies_keyed[current_frequency]) == 0:
            del frequencies_keyed[current_frequency]

    # add to proper frequency list
    try:
        frequencies_keyed[new_frequency].append(value)
    except KeyError:
        frequencies_keyed[new_frequency] = [value]

    # if we subtracted we might have changed the peak_frequency, need to recalculate
    # from the keys in frequencies_keyed, that's why we have two data structures
    if delta > 0:
        return max(peak_frequency, new_frequency)
    return max(frequencies_keyed.keys())
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

