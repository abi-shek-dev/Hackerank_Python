# You are given two arrays: A and B. Your task is to compute their inner product  and outer product.


import numpy as np

A=[list(map(int,input().split())) for _ in range(1)]

B=[list(map(int,input().split())) for _ in range(1)]

print(int(np.inner(A,B)))
print(np.outer(A,B))