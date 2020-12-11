from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        ground[Y][X] = 1

    warm = 0
    cabbage = deque()
    for x in range(N):
        for y in range(M):
            if ground[x][y]:
                ground[x][y] = 0
                cabbage.append((x, y))
                while cabbage:
                    x0, y0 = cabbage.popleft()
                    for n in range(4):
                        xn, yn = x0 + dx[n], y0 + dy[n]
                        if 0 <= xn < N and 0 <= yn < M:
                            if ground[xn][yn]:
                                ground[xn][yn] = 0
                                cabbage.append((xn, yn))
                warm += 1

    print(warm)