# You are given a 1-D array, A. Your task is to print the floor ,ceil  and rint of all the elements of A.

import numpy as np
x=list(map(float, input().split()))
np.set_printoptions(legacy='1.13')

print(np.floor(x))
print(np.ceil(x))
print(np.rint(x))