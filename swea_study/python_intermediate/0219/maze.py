import sys
sys.stdin = open('maze.txt')

def isWall(x, y):
    if 0 <= x < N and 0 <= y < N:
        return False
    return True

def dfs(x, y):
    global result
    visited[x][y] = 1
    if maze[x][y] == 3:
        result = 1
        return
    for n in range(4):
        if isWall(x+dx[n], y+dy[n]) == False:
            if maze[x+dx[n]][y+dy[n]] != 1 and visited[x+dx[n]][y+dy[n]] == 0:
                dfs(x+dx[n], y+dy[n])

T = int(input())
for tc in range(T):
    N = int(input())
    maze = []
    result = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for _ in range(N):
        maze.append(list(map(int, input())))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if maze[x][y] == 2:
                dfs(x, y)
           
    print('#{} {}'.format(tc+1, result))