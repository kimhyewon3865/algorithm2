import sys
sys.stdin = open("input.txt","rt")

arr = list(range(1,21))

for _ in range(10):
    startIdx, endIdx = map(int, input().split())

    for i in range( (endIdx-startIdx+1)//2 ):
        arr[startIdx+i-1], arr[endIdx-i-1] = arr[endIdx-i-1] , arr[startIdx+i-1]

for x in arr:
    print(x, end=' ')