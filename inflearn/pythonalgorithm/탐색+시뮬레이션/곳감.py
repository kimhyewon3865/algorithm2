n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    l, dir, c = map(int, input().split())

    if dir == 0:
        for i in range(c):
            arr[l-1].append(arr[l-1].pop(0))
        
    elif dir == 1:
        for i in range(c):
            arr[l-1].insert(0, arr[l-1].pop())

mIdx = n//2
res = 0
for i in range(n):
    
    if i > mIdx:
        idx = n - i -1
    else:
        idx = i    
    res += sum(arr[i][idx : n-idx])

print(res)