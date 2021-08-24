n = int(input())
lenArr = list(map(int, input().split()))
amtArr = list(map(int, input().split()))

res = 0
minAmt = 1e9

for len, amt in zip(lenArr, amtArr[:-1]):

    if minAmt > amt:
        minAmt = amt  

    res += minAmt * len
    
print(res)
'''
lt = 0
rt = 1
res = 0

while rt < n:
    if amtArr[lt] > amtArr[rt] or rt == (n-1) :
        res += (sum(lenArr[lt:rt]) * amtArr[lt])
        lt= rt
        rt += 1
    else:
        rt += 1
print(res)
'''

