dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def isWall(x, y):
    if 0 <= x < N and 0 <= y < N:
        return False
    return True

def dfs(x, y, k):
    global result
    if maze[x][y] == 3:
        result = k-1
        return
    visited[x][y] = 1
    for n in range(4):
        if isWall(x+dx[n], y+dy[n]) == False:
            if maze[x+dx[n]][y+dy[n]] != 1 and visited[x+dx[n]][y+dy[n]] == 0:
                dfs(x+dx[n], y+dy[n], k+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = []
    for _ in range(N):
        maze.append(list(map(int, input())))
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x0, y0 = i, j
    result = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dfs(x0, y0, 0)
    print('#{} {}'.format(tc, result))