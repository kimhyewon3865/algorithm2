m, n = 6, 4 #map(int,input().split())
picture = [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(picture, x,y, visited):

    if picture[x][y] != 0:     
        visited[x][y] = True
        dept = 0

        for i in range(4):
            if x+dx[i] < 0 or x+dx[i] >=m or y+dy[i] <0 or y+dy[i]>=n:
                # print('cont',x, y, i )
                continue
            if picture[x][y] == picture[x+dx[i]][y+dy[i]] and not visited[x+dx[i]][y+dy[i]]:
                dept += dfs(picture, x+dx[i], y+dy[i], visited) + 1

    return dept

visited = [[False] * n for _ in range(m)]
cnt = 0
maxDept = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j] and picture[i][j] != 0:
            cnt += 1
            dept = dfs(picture, i,j,visited) + 1
            if maxDept < dept:
                maxDept = dept


print(cnt, maxDept)
