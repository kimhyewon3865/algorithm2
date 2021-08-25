n, k = map(int, input().split())
arr = [i+1 for i in range(n)]
si = 0

while arr:
    if len(arr) == 1:
        print(arr.pop())
    else:
        si = (si+k-1)%len(arr)
        arr.pop(si)
