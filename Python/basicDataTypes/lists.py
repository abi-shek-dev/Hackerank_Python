# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by n lines of commands where each command will be of the n types listed above. Iterate through each command in order and perform the corresponding operation on your list.


if __name__ == '__main__':
    N = int(input())
    
    x=[]
    y=[]
    for i in range(N):
        x.append(input())

    for i in x:
        command=i.split(' ')
        if command[0] == 'insert':
            y.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(y)
        elif command[0] == 'remove':
            y.remove(int(command[1]))
        elif command[0] == 'append':
            y.append(int(command[1]))
        elif command[0] == 'sort':
            y.sort()
        elif command[0] == 'pop':
            y.pop()
        elif command[0] == 'reverse':
            y.reverse()