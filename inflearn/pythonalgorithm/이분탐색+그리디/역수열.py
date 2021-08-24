import sys
sys.stdin = open("input.txt","rt")

n = int(input())
arr = list(map(int, input().split()))
res = [0 for i in range(n)]

for i in range(n):
    tmpIdx = arr[i]

    if res[0:arr[i]].count(0) != arr[i]:
        while True:
            print("true", tmpIdx, res[tmpIdx])
            if res[tmpIdx] != 0:
                tmpIdx += 1
            else:
                res[tmpIdx] = i+1
                print("true else", tmpIdx, res[tmpIdx], res)
                break
    else:
        res[tmpIdx] = i+1
        print("else", tmpIdx, res[tmpIdx], res)

print(res)
            