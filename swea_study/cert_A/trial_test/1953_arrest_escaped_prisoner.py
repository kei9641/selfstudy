result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def isWall(x, y):
    if 0 <= x < N and 0 <= y < M:
        return False
    return True

def escape(x, y, h):
    visited[x][y] = h
    if h == L:
        return
    if underground[x][y] == 1:
        start, end, gap = 0, 4, 1
    elif underground[x][y] == 2:
        start, end, gap = 0, 2, 1
    elif underground[x][y] == 3:
        start, end, gap = 2, 4, 1
    elif underground[x][y] == 4:
        start, end, gap = 0, 4, 3
    elif underground[x][y] == 5:
        start, end, gap = 1, 4, 2
    elif underground[x][y] == 6:
        start, end, gap = 1, 3, 1
    elif underground[x][y] == 7:
        start, end, gap = 0, 3, 2
    for n in range(start, end, gap):
        if isWall(x+dx[n], y+dy[n]) == False:
            if visited[x+dx[n]][y+dy[n]] == 0 or visited[x+dx[n]][y+dy[n]] > h:
                if n == 0 and underground[x+dx[n]][y+dy[n]] in [1, 2, 5, 6]:
                    escape(x+dx[n], y+dy[n], h+1)
                elif n == 1 and underground[x+dx[n]][y+dy[n]] in [1, 2, 4, 7]:
                    escape(x+dx[n], y+dy[n], h+1)
                elif n == 2 and underground[x+dx[n]][y+dy[n]] in [1, 3, 4, 5]:
                    escape(x+dx[n], y+dy[n], h+1)
                elif n == 3 and underground[x+dx[n]][y+dy[n]] in [1, 3, 6, 7]:
                    escape(x+dx[n], y+dy[n], h+1)

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    underground = []
    for _ in range(N):
        underground.append(list(map(int, input().split())))
    move = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    escape(R, C, 1)
    for x in range(N):
        for y in range(M):
            if visited[x][y] > 0:
                move += 1
    
    result.append(move)
for i in range(T):
    print('#{} {}'.format(i+1, result[i]))
