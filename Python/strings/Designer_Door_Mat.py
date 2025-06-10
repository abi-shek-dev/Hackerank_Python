# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N X M. (N is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

n,m=map(int,input().split())
s1='-'
s='.|.'
c=(m-3)//2
for i in range(0,n//2):
    print(s1*c+s*(2*i+1)+s1*c)
    c-=3
print(s1*((m-7)//2)+'WELCOME'+s1*((m-7)//2))
c=3
for i in range((n//2)-1,-1,-1):
    print(s1*c+s*(2*i+1)+s1*c)
    c+=3