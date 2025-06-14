# You are given two integer arrays, A and B of dimensions NXM.
# Your task is to perform the following operations:

# Add ( A+ B)
# Subtract (A -B )
# Multiply (A *B )
# Integer Division (A / B)
# Mod ( A% B)
# Power ( A**B )

import numpy as np

n,m = map(int, input().split())

A=[list(map(int, input().split()))for _ in range(n)]

B=[list(map(int, input().split()))for _ in range(n)]

a=np.array(A)
b=np.array(B)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)