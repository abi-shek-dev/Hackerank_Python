# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

x,y =input().split()
y=int(y)



for i in range (1,y+1):
    
    z=[]
    
    com = list(combinations(x,i))
    
    for j in com:
        j=list(j)
        j.sort()
        z.append(''.join(j))
    
    z.sort()
    
    for j in z:
        print(j)