# You are given a N X M integer array matrix with space separated elements (N = rows and M  = columns).
# Your task is to print the transpose and flatten results.

import numpy as np

def transpose(matrix):
    np_matrix = np.array(matrix)
    return np_matrix.transpose()

def flatten(matrix):
    np_matrix = np.array(matrix)
    return np_matrix.flatten()

r, c = map(int, input().split())

x = []
for _ in range(r):
    row = list(map(int, input().split()))
    x.append(row)

transposed = transpose(x)
flattened = flatten(x)
print(transposed)
print(flattened)
