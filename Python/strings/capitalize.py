import math
import os
import random
import re
import sys
def solve(s):
    return ''.join(c.capitalize() if i == 0 or s[i-1] == ' ' else c for i, c in enumerate(s))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
