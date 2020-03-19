#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_tally = Counter(a)
    b_tally = Counter(b)

    removals = 0
    for letter, frequency in a_tally.items():
        if letter not in b_tally:
            removals += frequency
        else:
            # b also has this letter
            # remove the difference between this letter's frequency in b and a
            removals += abs(frequency - b_tally[letter])
            # letter already considered in b, delete it so we can check later if there are leftover letters in b
            del b_tally[letter]
    
    # add the remaining items by frequency left in b
    removals += sum([frequency for frequency in b_tally.values()])

    return removals


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

