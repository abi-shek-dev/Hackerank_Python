# You are given a 2-D array of size N x M.

# Your task is to find:
#     1. The mean along axis 1.
#     2. The variance along axis 0.
#     3.The standard deviation along axis none


import numpy as np

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

arr=np.array(data)

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr),11))