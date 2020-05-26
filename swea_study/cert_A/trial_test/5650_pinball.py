dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
back = [1, 0, 3, 2]
a = []

def go(x0, y0, d):
    global result
    point = 0
    x = x0 + dx[d]
    y = y0 + dy[d]
    while 1:
        # 벽이면 point+1, 반대로 턴
        if not (0 <= x < N and 0 <= y < N):
            point += 1
            d = back[d]
        else:
            obj = board[x][y]
            # 원위치거나 블랙홀이면 최대값 저장 후 종료
            if (x, y) == (x0, y0) or obj == -1:
                if point > result:
                    result = point
                return
            # 웜홀이면 반대편으로 이동후 같은 방향으로 한칸 전진
            elif obj > 5:
                # 둘 중 다른 쪽 웜홀 위치를 저장
                for i in range(2):
                    if warmhole[obj][i] != (x, y):
                        x, y = warmhole[obj][i]
                        break
            # 장애물
            elif obj:
                point += 1
                # 상
                if d == 0:
                    if obj == 1 or obj == 4 or obj == 5:
                        d = back[d]
                    elif obj == 2:
                        d = 3
                    elif obj == 3:
                        d = 2
                # 하
                elif d == 1:
                    if obj == 2 or obj == 3 or obj == 5:
                        d = back[d]
                    elif obj == 1:
                        d = 3
                    elif obj == 4:
                        d = 2
                # 좌
                elif d == 2:
                    if obj == 3 or obj == 4 or obj == 5:
                        d = back[d]
                    elif obj == 1:
                        d = 0
                    elif obj == 2:
                        d = 1
                # 우
                elif d == 3:
                    if obj == 1 or obj == 2 or obj == 5:
                        d = back[d]
                    elif obj == 4:
                        d = 0
                    elif obj == 3:
                        d = 1
        x += dx[d]
        y += dy[d]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    warmhole = [[] for _ in range(11)]
    
    # 웜홀 위치 찾기
    for x in range(N):
        for y in range(N):
            if board[x][y] > 5:
                warmhole[board[x][y]].append((x, y))

    # 0인 위치부터 탐색
    for x in range(N):
        for y in range(N):
            if not board[x][y]:
                # 4방향
                for n in range(4):
                    go(x, y, n)

    print('#{} {}'.format(tc, result))
