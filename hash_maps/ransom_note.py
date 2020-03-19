#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_hash = {}

    for word in magazine:
        # consider a word can't be used twice for just one key, so we increment/decrement
        # instead of a straight up Yes/No value
        if not magazine_hash.get(word, False):
            magazine_hash[word] = 0
        magazine_hash[word] += 1
    
    for word in note:
        if word not in magazine_hash:
            print('No')
            return
        else:
            magazine_hash[word] -= 1
        if magazine_hash[word] < 0:
            print('No')
            return
        
    print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

