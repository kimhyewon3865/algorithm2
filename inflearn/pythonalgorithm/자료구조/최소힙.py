import heapq

i = 0
arr = []

while True:
    i = int(input())
    if i == 0:
        print(-heapq.heappop(arr))
    elif i == -1:
        break
    else:
        heapq.heappush(arr, i)
    print(arr)


# while True:
#     i = int(input())
#     if i == 0:
#         arr.sort()
#         print(arr.pop(0))
#     elif i == -1:
#         break
#     else:
#         arr.append(i)
