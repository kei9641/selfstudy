import sys
sys.stdin = open('최소생산비용(5209).txt')

def dfs(x, cost):
    global result
    if x == N:
        if result > cost:
            result = cost
        return
    if cost >= result:
        return
    for y in range(N):
        if visited[y] == 0:
            visited[y] = 1
            dfs(x+1, cost+factory[x][y])
            visited[y] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = 1500
    dfs(0, 0)
    print('#{} {}'.format(tc, result))