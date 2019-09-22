#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if (a[j] > a[j + 1]):
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
                count += 1

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fptr.write('Array is sorted in ' + str(count) + ' swaps.\n')
    fptr.write('First Element: ' + str(a[0]) + '\n')
    fptr.write('Last Element: ' + str(a[len(a) - 1]) + '\n')

    fptr.close()

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
