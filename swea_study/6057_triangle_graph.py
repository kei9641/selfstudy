T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    visited = [0 for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x-1][y-1] = 1
        graph[y-1][x-1] = 1

    triangle = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if graph[i][j] == 1 and graph[j][k] == 1 and graph[k][i] == 1:
                    triangle += 1
    print('#{} {}'.format(tc+1, triangle))