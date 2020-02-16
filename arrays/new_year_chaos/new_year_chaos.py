#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    """Function Description

    Complete the function minimumBribes in the editor below. It must print an integer 
    representing the minimum number of bribes necessary, or Too chaotic if the line 
    configuration is not possible.

    minimumBribes has the following parameter(s):

    q: an array of integers"""
    bribes = 0
    unknown_list = []
    for i in range(len(q)):
        score = calculate_score(i, q[i])
        if score > 2:
            # busted
            print("Too chaotic")
            return
        elif score == 0:
            # probably did not move
            unknown_list.append(q[i])
        elif 0 < score <= 2:
            # this dude bribed to be here
            bribes += score
        else:
            # probably didn't bribe, but we will know for sure in the bubble sort later
            unknown_list.append(q[i])
    
    # at this point, the obvious bribers were removed and their bribes calculated
    # go through the list and bubble sort, for each switch, increment bribes
    found_briber = True # assume we have at least a briber
    while found_briber:
        found_briber = False
        for i in range(len(unknown_list) - 1):  # -1 because next will always be + 1
            current = unknown_list[i]
            next_number = unknown_list[i+1]
            if current > next_number:
                # current bribed
                bribes += 1
                found_briber = True
                unknown_list[i], unknown_list[i+1] = unknown_list[i+1], unknown_list[i]

    # if we got here we are done, the remaining list is sorted and we calculated
    # all bribes
    print(bribes)



def calculate_score(current_index, value):
    start_index = value - 1
    return  start_index - current_index
    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
