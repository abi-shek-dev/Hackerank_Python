# You are given a 2-D array with dimensions N x M.
# Your task is to perform the min function over axis 1 and then find the max of that.


import numpy as np

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

arr = np.array(data)

row_mins = np.min(arr, axis=1)

result = np.max(row_mins)

print(result)
