#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    h = [0, 0, 0, 1, 2, 2, 2]
    w = [0, 1, 2, 1, 0, 1, 2]

    hourglass_sums = []

    for j in range(4):
        # walk 4 times vertically
        for k in range(4):
            # walk 4 times horizontally
            hourglass = 0
            for i in range(7):
                first_dimension_index = h[i]
                second_dimension_index = w[i]
                hourglass += arr[first_dimension_index][second_dimension_index]
            hourglass_sums.append(hourglass)
            w = increment_dimension(w)
        w = reset_dimension(w)
        h = increment_dimension(h)
    
    return(max(hourglass_sums))


def increment_dimension(d):
    return [i + 1 for i in d]


def reset_dimension(d):
    return [i - 4 for i in d]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

