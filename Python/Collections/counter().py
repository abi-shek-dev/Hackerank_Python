
from collections import Counter

x = int(input())                       
sizes = list(map(int, input().split())) 
n = int(input())                       

shoe_count = Counter(sizes)
money_earned = 0

for _ in range(n):
    size, price = map(int, input().split())
    if shoe_count[size] > 0:      
        money_earned += price    
        shoe_count[size] -= 1     

print(money_earned)
