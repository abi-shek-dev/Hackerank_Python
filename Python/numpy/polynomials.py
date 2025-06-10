# You are given the coefficients of a polynomial P
# Your task is to find the value of P at a given point x.


import numpy as np

P=[float(x) if '.' in x else int(x) for x in input().split()]

x=int(input())

print(np.polyval(P,x))