result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def route(x, y, trail, K):
    global maxCourse
    visited[x][y] = 1
    if maxCourse < trail:
        maxCourse = trail
    for i in range(4):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N:
            if visited[x+dx[i]][y+dy[i]] == 0:
                if mountain[x][y] > mountain[x+dx[i]][y+dy[i]]:
                    route(x+dx[i], y+dy[i], trail+1, K)
                elif mountain[x+dx[i]][y+dy[i]] - K < mountain[x][y]:
                    pre = mountain[x+dx[i]][y+dy[i]]
                    mountain[x+dx[i]][y+dy[i]] = mountain[x][y] - 1
                    route(x+dx[i], y+dy[i], trail+1, 0)
                    mountain[x+dx[i]][y+dy[i]] = pre
    visited[x][y] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    top = 0
    start = []
    maxCourse = 0
    for x in range(N):
        for y in range(N):
            if top < mountain[x][y]:
                start = []
                top = mountain[x][y]
            if top == mountain[x][y]:
                start.append(x)
                start.append(y)
    for i in range(0, len(start), 2):
        route(start[i], start[i+1], 1, K)
    result.append(maxCourse)

for i in range(T):
    print('#{} {}'.format(i+1, result[i]))