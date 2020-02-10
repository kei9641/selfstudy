import sys
sys.stdin = open('telecom.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    map = []
    for _ in range(N):
        map.append(list(input()))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def isWall(x, y):
        if 0 <= x < N and 0 <= y < N:
            return False
        return True

    count = 0
    for x in range(N):
        for y in range(N):
            if map[x][y] == 'A':
                for i in range(4):
                    if isWall(x + dx[i], y + dy[i]) == False:
                        map[x + dx[i]][y + dy[i]] = 'X'
            elif map[x][y] == 'B':
                for i in range(4):
                    for n in range(1,3):
                        if isWall(x + dx[i]*n, y + dy[i]*n) == False:
                            map[x+dx[i]*n][y+dy[i]*n] = 'X'
            elif map[x][y] == 'C':
                for i in range(4):
                    for n in range(1, 4):
                        if isWall(x + dx[i] * n, y + dy[i] * n) == False:
                            map[x + dx[i] * n][y + dy[i] * n] = 'X'

    for x in range(N):
        for y in range(N):
            if map[x][y] == 'H':
                count += 1
    print('#{} {}'.format(tc+1, count))