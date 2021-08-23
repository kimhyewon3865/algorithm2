import sys
sys.stdin=open("input.txt", "rt")

n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()

res = 0
start = 0
end = n-1

while start < end:
    
    if m >= (arr[end] + arr[start]):
        res += 1
        start += 1
        end -= 1
    else:
        res += 1
        end -= 1

print(res)  