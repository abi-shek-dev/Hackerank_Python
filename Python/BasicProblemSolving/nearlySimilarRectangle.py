#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


def nearlySimilarRectangles(sides):
    

    ratio_count = defaultdict(int)

    for w, h in sides:
        gcd = math.gcd(w, h)
        ratio = (w // gcd, h // gcd)
        ratio_count[ratio] += 1

    count = 0
    for val in ratio_count.values():
        count += val * (val - 1) // 2

    return count

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sides_rows = int(input().strip())
    sides_columns = int(input().strip())

    sides = []
    
    for _ in range(sides_rows):
        sides.append(list(map(int, input().rstrip().split())))

    result = nearlySimilarRectangles(sides)

    fptr.write(str(result) + '\n')

    fptr.close()