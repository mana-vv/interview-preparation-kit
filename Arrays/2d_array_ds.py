#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    ret = None

    for j in range(4):
        for i in range(4):
            total = arr[j][i] + arr[j][i + 1] + arr[j][i + 2] \
                + arr[j + 1][i + 1] \
                + arr[j + 2][i] + arr[j + 2][i + 1] + arr[j + 2][i + 2]
            if ret == None or total > ret: 
                ret = total
    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
