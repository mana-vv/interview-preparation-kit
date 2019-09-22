#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter

# Complete the luckBalance function below.
def luckBalance(k, contests):
    ret = 0
    contests.sort(key=itemgetter(1, 0), reverse=True)
    for i in range(len(contests)):
        if contests[i][1] == 0 or i < k:
            ret += contests[i][0]
        else:
            ret -= contests[i][0]
    return ret

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
