# You are given a square matrix A with dimensions N X N. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.


import numpy as np

N=int(input())

P = [list(map(float, input().split())) for _ in range(N)]

print(round(np.linalg.det(P),2))