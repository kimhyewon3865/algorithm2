import collections
str1 = list(input())
str2 = list(input())

res = collections.Counter(str1) - collections.Counter(str2)

if res:
    print("no")
else:
    print("yes")