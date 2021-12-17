#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count=0
    for i in range (0, len(a) - 1):
        for j in range(0, len(a) - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count +=1
    print("Array is sorted in {} swaps.".format(count))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
if __name__ == '__main__':
    n = int(raw_input().strip())

    a = map(int, raw_input().rstrip().split())

    countSwaps(a)
