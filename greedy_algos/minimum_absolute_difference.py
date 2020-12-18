#!/bin/python3

import math
import os
import random
import re
import sys


def absolute_difference(a, b):
    return abs(a - b)


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    # Complete the minimumAbsoluteDifference function in the editor below.
    # It should return an integer that represents the minimum absolute
    # difference between any pair of elements.
    arr.sort()
    # now the list is sorted so we just need to test every item and next neighbour
    # keeping track of the lowest diff
    current_index = 0
    next_index = 1
    min_abs_diff = math.inf
    while next_index < len(arr):
        min_abs_diff = min(min_abs_diff, absolute_difference(arr[current_index], arr[next_index]))
        current_index += 1
        next_index += 1
    return min_abs_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
