# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w. 

import textwrap

def wrap(string, max_width):
    
    x=textwrap.fill(string, max_width)
    
    return x

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)