def isWall(x, y):
    if 0 <= x < N and 0 <= y < N:
        return False
    return True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
apartment = 0

def dfs(x, y):
    global apartment
    visited[x][y] = 1
    apartment += 1
    # print(apartment)
    for n in range(4):
        if isWall(x+dx[n], y+dy[n]) == False:
            if city[x+dx[n]][y+dy[n]] == 1 and visited[x+dx[n]][y+dy[n]] == 0:
                dfs(x+dx[n], y+dy[n])

N = int(input())
city = []
for _ in range(N):
    city.append(list(map(int, input())))
visited = [[0 for _ in range(N)] for _ in range(N)]
complexes = []
for x in range(N):
    for y in range(N):
        if city[x][y] == 1 and visited[x][y] == 0:
            apartment = 0
            dfs(x, y)
            complexes.append(apartment)
complexes.sort()
print(len(complexes))
for i in range(len(complexes)):
    print(complexes[i])

'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''