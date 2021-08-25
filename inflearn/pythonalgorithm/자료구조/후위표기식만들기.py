arr = input()
stack=[]
for x in arr:
    if x.isdecimal():
        stack.append(int(x))
    elif x == '(' or x == ')':
        continue
    else: 
        n1 = stack.pop()
        n2 = stack.pop()
        if x == '+':
            stack.append(n2 + n1)
        elif x == '-':
            stack.append(n2 - n1)
        elif x == '*':
            stack.append(n2 * n1)
        elif x == '/':
            stack.append(n2 / n1)
            
print(stack.pop())