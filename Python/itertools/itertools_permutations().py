# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

x,y=input().split()
y=int(y)
z=[]

per=list(permutations(x,y))

for i in per:
    z.append(''.join(i))

z.sort()

for i in z:
    print(i)