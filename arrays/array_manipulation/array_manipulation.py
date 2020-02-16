#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    mutations = {}
    for query in queries:
        start_index = query[0]
        end_index = query[1]
        increment = query[2]
        initialize_position(mutations, start_index, end_index)
        set_increment_boundaries(mutations, start_index, end_index, increment)

    # now go through our beautiful fresh data structure adding and subtracting
    # as we go through the "boundaries"
    indices = [index for index in mutations.keys()]
    sorted_indices = sorted(indices)

    current = 0
    peak = 0
    for index in sorted_indices:
        increments = mutations[index]
        for inc in increments:
            current += inc
        if current > peak:
            peak = current
    return peak


def initialize_position(mutations, start_index, end_index):
    for index in [start_index, end_index + 1]:
        if not mutations.get(index, False):
            mutations[index] = []

def set_increment_boundaries(mutations, start_index, end_index, increment):
    mutations[start_index].append(increment)
    # since it's inclusive we start decrementing from the next position
    mutations[end_index + 1].append(-increment)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
