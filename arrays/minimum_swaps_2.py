#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    """We flip value at current index to the proper position.
    If already proper, increment until the end of the array once
    """
    swaps = 0
    i = 0
    while i < len(arr) - 1: # skip last one
        value = arr[i]
        proper_index = value - 1
        if proper_index != i:
            swap(arr, i, proper_index)
            swaps += 1
        else:
            i += 1
    return swaps

def swap(arr, actual_index, proper_index):
    arr[actual_index], arr[proper_index] = arr[proper_index], arr[actual_index]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
