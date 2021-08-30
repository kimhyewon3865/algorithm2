import collections
from typing import Collection

arr = [list(map(int,input().split())) for _ in range(9)]

def check(arr): 
    i, j =0,0
    
    for idx in range(9):
        c = collections.Counter(arr[idx])
        if any(v != 1 for v in c.values()):
            return False

        c = collections.Counter(arr[0:9][idx])
        if any(v != 1 for v in c.values()):
            return False

    for i in range(3):
        for j in range(3):
            c = collections.Counter(arr[i*3][j*3:j*3+3]+arr[i*3+1][j*3:j*3+3]+arr[i*3+2][j*3:j*3+3] )
            if any(v != 1 for v in c.values()):
                return False
    return True

if check(arr):
    print("YES")
else:
    print("NO")