def dfs(x):
    global cnt, route
    if route < cnt:
        route = cnt
    for y in range(N):
        if visited[y] == 0 and arr[x][y] == 1:
            visited[y] = 1
            cnt += 1
            dfs(y)
            visited[y] = 0
            cnt -= 1            

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        arr[x-1][y-1] = 1
        arr[y-1][x-1] = 1
    visited = [0 for _ in range(N)]
    route = 0
    for i in range(N):
        cnt = 1
        visited[i] = 1
        dfs(i)
        visited[i] = 0
    print('#{} {}'.format(tc, route))