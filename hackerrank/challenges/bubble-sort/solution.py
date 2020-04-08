#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    arr, swaps = sort(a)

    print('Array is sorted in {} swaps.'.format(swaps))
    print('First Element: {}'.format(arr[0]))
    print('Last Element: {}'.format(arr[-1]))


def sort(a):
    swaps = 0
    arr = a
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps = swaps + 1
    return arr, swaps

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
