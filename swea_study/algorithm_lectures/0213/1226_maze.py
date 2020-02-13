import sys
sys.stdin = open('maze.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x0, y0):
    visited[x0][y0] = 1
    
    for i in range(4):
        if maze[x0+dx[i]][y0+dy[i]] == 3:
            return 1
        if maze[x0+dx[i]][y0+dy[i]] == 0 and visited[x0+dx[i]][y0+dy[i]] == 0:
            dfs(x0+dx[i], y0+dy[i])
        return 0



for _ in range(10):
    tc = int(input())
    maze = []
    for _ in range(16):
        maze.append(list(map(int, input())))
    visited = [[0 for _ in range(16)] for _ in range(16)]
    # for i in range(16):
    #     print(*maze[i])
    # print()
    
    print(dfs(1, 1))

