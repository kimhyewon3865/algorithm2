import collections

n = int(input())

note = [input() for _ in range(n)]
poem = [input() for _ in range(n-1)]


res = (collections.Counter(note) - collections.Counter(poem))

# for key in res.keys():
#     print(key)

print(res.keys())
