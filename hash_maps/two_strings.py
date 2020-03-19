2#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1_map = {}
    s1_key_counter = 0
    WORDS_IN_CONSTRAINT = 26    # ascii[a-z]

    for c in s1:
        if c not in s1_map:
            s1_map[c] = True
            s1_key_counter += 1
            if s1_key_counter == WORDS_IN_CONSTRAINT:
                break   # got all letters already, stop indexing
    
    for c in s2:
        if c in s1_map:
            return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

