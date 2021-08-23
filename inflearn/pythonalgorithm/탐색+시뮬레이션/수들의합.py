import sys
sys.stdin = open("input.txt","rt")

n, m = map(int,input().split())
arr = list(map(int, input().split()))

res = 0
for i in range(n):
    tmp = 0
    for j in range(i,n):
        if tmp <= m:
            tmp += arr[j]
            if tmp == m:
                res += 1
                break            
        else:
            break
print(res)