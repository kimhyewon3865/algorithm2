priorities=[2, 1, 3, 2]
location = 2
answer = 0

# for _ in range(location):
#     cul = priorities.pop(0)
#     priorities.append(cul)
    # print(priorities)



while priorities:

    print(priorities, location )

    cul = priorities.pop(0)

    if all(cul >= x for x in priorities):
            answer += 1
            if location == 0:
                break

    else:
        priorities.append(cul)

    location = (location-1+len(priorities)) % len(priorities)

print(answer)