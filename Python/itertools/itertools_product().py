
from itertools import product

a=list(map(int,input().split(" ")))
b=list(map(int,input().split(" ")))

c=[a,b]

d=list(product(*c))

for i in d:
    print(i,end=" ")