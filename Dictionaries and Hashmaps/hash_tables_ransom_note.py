#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    return Counter(note) - Counter(magazine) == {}
        

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    if checkMagazine(magazine, note):
        result = "Yes"
    else:
        result = "No"
    fptr.write(str(result) + '\n')


