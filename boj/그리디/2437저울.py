n = int(input())
arr = list(map(int, input().split()))

i = 1
while i < 30:
    if i in arr:
        print('1if' , i)
        i+=1
    
    else:
        for n in arr:
            if i-n in arr:
                print('2iff', i)
                i += 1
                break
        else:
            print('res', i)
            break
     