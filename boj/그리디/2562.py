arr= []

for i in range(9):
    arr.append( (int(input()), i+1)) 

arr.sort(reverse=True)

print(arr[0][0])
print(arr[0][1])

