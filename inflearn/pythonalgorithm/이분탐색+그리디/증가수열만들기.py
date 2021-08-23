import sys
# from collections import deque
sys.stdin=open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

# arr = deque(arr)

last=0
res = ""
dic = {}

while arr:

    dic = {arr[0]: 'L', arr[-1]: 'R'}
    minKey = min(arr[0], arr[-1])
    if minKey > last:
        if dic[minKey] == 'L':
            arr.pop(0)
            res += 'L'
            
        else :
            arr.pop()
            res += 'R'
        last = minKey
        
    else:
        break

print(len(res))
print(res)
        

