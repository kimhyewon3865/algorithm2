from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr = deque(arr)
cnt = 0

while True:
    tmp = arr.popleft()
    if max(arr) != arr[0]:
        arr.append(tmp)
        
    else:
        cnt += 1
        if m == 0:
            print(cnt)
            break

    m = (m-1+len(arr))%len(arr)
    