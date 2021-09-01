from collections import deque

arr = input()
n = int(input())

for i in range(n):

    plan = input()
    dq = deque(arr)

    for a in plan:
        if a in dq:
            if a != dq.popleft():
                print("NO")
                break
    else:
        if len(dq) == 0:
            print("YES")
        else:
            print("NO")




# for i in range(n):

#     arr2 = input()
#     tmp = ""
#     for a in arr2:
#         if a in arr :
#             tmp += a

#     if arr == tmp:
#         print("YES")
#     else:
#         print("NO")

