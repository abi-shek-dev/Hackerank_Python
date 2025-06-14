# Given an integer,n , and n space-separated integers as input, create a tuple,t , of those n integers. Then compute and print the result of hash(t).

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.


n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))

# python 2 version of the code:

# if __name__ == '__main__':
#     n = int(raw_input())
#     t = tuple(map(int, raw_input().split()))
#     print hash(t)