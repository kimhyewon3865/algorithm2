n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]

res = []

tmp1 = 0
tmp2 = 0

for i in range(n):
    
    res.append( sum(arr[i][0:n]))
    res.append( sum(arr[0:n][i]))

    tmp1 += arr[i][i]
    tmp2 += arr[i][n-i-1]

res.append(tmp1)
res.append(tmp2)

print(max(res))