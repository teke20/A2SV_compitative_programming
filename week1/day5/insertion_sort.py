#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    # 2 4 6 8 3
    temp = arr[-1]
    j = n - 1
    while j>0 and arr[j-1]> temp:
        arr[j] = arr[j-1]
        print(*arr)
        j -= 1
    arr[j] = temp
    print(*arr)
        
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
