students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
answer = list(map(int,input().split()))

res = [0,0,0]

for i in range(len(answer)):
    for j in range(3):
        print(i, j, students[j][i%len(students[j])],answer[i],res[j])
        if students[j][i%len(students[j])] == answer[i]:
            res[j] += 1
            print(i,j)
            
res2 = []
for i in range(3):
    if all(res[i] >= n for n in res):
        res2.append(i+1)

res2.sort()
print(res2)