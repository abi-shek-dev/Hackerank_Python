# You are given two arrays A and B. Both have dimensions of N X N.
# Your task is to compute their matrix product.


import numpy as np

n=int(input())

A=[list(map(int,input().split())) for _ in range(n)]
B=[list(map(int,input().split())) for _ in range(n)]

A=np.array(A)
B=np.array(B)

print(np.dot(A,B))