# You are given two integer arrays of size N X P and M X P (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.

# Input Format

# The first line contains space separated integers N, M and P.
# The next N lines contains the space separated elements of the P columns.
# After that, the next M lines contains the space separated elements of the P columns.

# Output Format

# Print the concatenated array of size (N+M) X P.

import numpy as np

N, M, P = map(int, input().split())

array1 = [list(map(int, input().split())) for _ in range(N)]

array2 = [list(map(int, input().split())) for _ in range(M)]

a1 = np.array(array1)
a2 = np.array(array2)

result = np.concatenate((a1, a2), axis=0)

print(result)
