n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

mIdx = n//2
res = 0

for i in range(n):
    
    if i > mIdx:
        idx = n - i -1
    else:
        idx = i    
    res += sum(arr[i][mIdx-idx : mIdx +idx+1])  

print(res)