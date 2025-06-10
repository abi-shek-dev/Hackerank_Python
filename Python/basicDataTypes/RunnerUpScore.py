# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split()))]
    
    max_arr=max(arr[0])
    arr[0] = list(set(arr[0]))
    for i in arr[0]:
        if i == max_arr:
            arr[0].remove(i)
  
    print(max(arr[0]))