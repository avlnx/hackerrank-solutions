#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, namedtuple

# Complete the isValid function below.
def isValid(s):
    s_tally = Counter(s)

    frequencies_tally = Counter(s_tally.values())

    if len(frequencies_tally) == 1:
        # all have the same frequency
        return 'YES'
    elif len(frequencies_tally) == 2:
        CharFrequency = namedtuple('CharFrequency', 'char_freq num_chars_with_freq')
        
        # create namedtuples of frequencies for improved readability
        freqs = [CharFrequency(char_freq, num_chars_with_freq) for char_freq, num_chars_with_freq in frequencies_tally.items()]

        # if one of the items happens only once and only with a frequency of one we can just remove it
        for f in freqs:
            if f.char_freq == 1 and f.num_chars_with_freq == 1:
                return 'YES'
        
        # sort list of CharFrequency namedtuples by the num_chars_with_freq descending
        freqs = sorted(freqs, key=lambda x: x[1], reverse=True)
        most_frequent = freqs[0]
        underdog = freqs[1]

        # if the frequencies differ by one and the underdog has only one char we're good
        frequency_diff = abs(most_frequent.char_freq - underdog.char_freq)
        if frequency_diff > 1:
            return 'NO'
        else:
            # frequency is adjustable by one, check if we only have one occurence of
            # the underdog frequency and we're good
            if underdog.num_chars_with_freq > 1:
                return 'NO'
            return 'YES'
    
    # all other cases we fail
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

