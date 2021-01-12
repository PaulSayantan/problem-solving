#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    a = a[::-1]
    return a

if __name__ == '__main__':

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(' '.join(map(str, res)))
    print('\n')
