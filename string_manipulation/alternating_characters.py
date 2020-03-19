#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    if len(s) == 0:
        return 0
    removals = 0
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            removals += 1
        else:
            current_char = s[i]
    return removals


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

