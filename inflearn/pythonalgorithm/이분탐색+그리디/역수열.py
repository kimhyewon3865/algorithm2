import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
arr = list(map(int, input().split()))
res = []

for i in range(n-1,-1,-1):
    idx = arr[i]
    if idx >= len(res):
        res.append(i+1)
    else:
        res.insert(idx, i+1)

for x in res:
    print(x, end = ' ')
