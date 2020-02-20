T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x-1][y-1] = 1
        graph[y-1][x-1] = 1
    for i in range(N):
        print(*graph[i])