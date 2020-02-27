import sys
sys.stdin open('pipe_connect.txt')

def isWall(x,y):
    if 0 <= x < N and 0 <= y < N:
        return False
    return True

def dfs(x, y):
    visited[x][y] = 1


T = int(input())
for tc in range(T):
    N = int(input())
    area = []
    for _ in range(N):
        area.append(list(map(int, input().split())))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[0][0] = 1
    if area[0][0] == 1:
        dfs(0, 1)
    else:
        dfs(1, 0)
