'''
4 [1,2,9,3,10,8,4,5,6,7]
5 [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
6 [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
'''

n = 6
arr = []
for i in range(1, n+1):
    arr.append([0]*i)
num =1

x1, y1 = 0,0
x2, y2 = n-1 , 1
x3, y3 = n-2, n-2

while n>0:
    for i in range(n):
        arr[x1+i][y1] = num
        num += 1
    x1+=2
    y1+=1
    for i in range(n-1):
        arr[x2][y2+i] = num
        num += 1
    x2-=1
    y2+=1
    for i in range(n-2):
        arr[x3-i][y3-i] = num
        num += 1
    x3-=1
    y3-=2
    n-=3

res = []
for array1 in arr:
    for n in array1:
        res.append(n)

print(res)