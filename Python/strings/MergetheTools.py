def merge_the_tools(string, k):
    x=[]
    for i in range(0,len(string),k):
        a=string[i:i+k]
        b=""
        for j in a:
            if j not in b:
                b+=j
        x.append(b)
    print("\n".join(x))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)