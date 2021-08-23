import sys
sys.stdin = open("input.txt","rt")

n = int(input())
nArr = list(map(int, input().split()))
m = int(input())
mArr = list(map(int, input().split()))

newArr = nArr + mArr
newArr.sort()

for x in newArr:
    print(x, end=' ')
