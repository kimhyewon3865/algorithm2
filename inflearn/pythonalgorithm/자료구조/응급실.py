from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr = deque(arr)
cnt = 0

while True:
    
    if max(arr) != arr[0]:
        tmp = arr.popleft()
        arr.append(tmp)
        
    else:
        arr.popleft()
        cnt += 1
        if m == 0:
            print(cnt)
            break

    m = (m-1+len(arr))%len(arr)
    