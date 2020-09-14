#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List, Callable
from itertools import takewhile


# Complete the plusMinus function below.
def plusMinus(arr):
  arr = sorted(arr)
  negative_count = count_on_rule(lambda x: x < 0, arr)
  zero_count = count_on_rule(lambda x: x == 0, arr[negative_count:])
  total_count = len(arr)
  positive_count = total_count - negative_count - zero_count
  [print_result(n, total_count)
    for n in (positive_count, negative_count, zero_count)]


def print_result(count: int, total: int) -> None:
  print(f"{round(count / total, 6)}")


def count_on_rule(rule: Callable[[int], int], arr: List[int]) -> int:
  return len(list(takewhile(rule, arr)))


if __name__ == '__main__':
  n = int(input())

  arr = list(map(int, input().rstrip().split()))

  plusMinus(arr)
