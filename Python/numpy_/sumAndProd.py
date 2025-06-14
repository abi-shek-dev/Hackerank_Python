# You are given a 2-D array with dimensions NXM.
# Your task is to perform the sum tool over axis 0 and then find the product of that result.


import numpy as np
n, m = map(int, input().split())

arr = np.array([list(map(int, input().split())) for _ in range(n)])
sum_result = np.sum(arr, axis=0)
print(np.prod(sum_result))