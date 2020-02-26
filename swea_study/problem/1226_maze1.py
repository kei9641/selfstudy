def dfs(x0, y0):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    global ans
    if ans == 1:
        return
    visited[x0][y0] = 1
    for i in range(4):
        if maze[x0+dx[i]][y0+dy[i]] != 1 and visited[x0+dx[i]][y0+dy[i]] == 0:
            if maze[x0+dx[i]][y0+dy[i]] == 3:
                ans = 1
            else:
                dfs(x0+dx[i], y0+dy[i])

for _ in range(10):
    tc = int(input())
    maze = []
    visited = [[0 for _ in range(16)] for _ in range(16)]
    for _ in range(16):
        maze.append(list(map(int, input())))
    ans = 0
    dfs(1, 1)
    print('#{} {}'.format(tc, ans))