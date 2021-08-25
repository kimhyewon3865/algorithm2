arr = list(input())

stack = []
res = 0

for i, c in enumerate(arr):
    if c == '(':
        stack.append('(')
    elif c == ')':
        stack.pop()
        if arr[i-1] == '(': #레이저
            res += len(stack)
        else: #쇠막대기 끝위치
            res += 1
        
print(res)