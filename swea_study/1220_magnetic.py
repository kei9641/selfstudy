import sys
sys.stdin = open('magnetic.txt')

T = 10
for tc in range(T):
    N = int(input())
    table = []
    deadlock = 0
    for _ in range(N):
        table.append(list(map(int, input().split())))
    for y in range(N):
        for x in range(N):
            # 위에서 S극 제거
            if table[x][y] == 1:
                break
            elif table[x][y] == 2:
                table[x][y] = 0
    for y in range(N):
        for x in range(N-1, -1, -1):
            # 아래에서 N극 제거
            if table[x][y] == 2:
                break
            elif table[x][y] == 1:
                table[x][y] = 0

    # 위쪽으로 모으기
    for y in range(N):
        for x in range(N):
            if table[x][y] == 0:
                for n in range(1, N-x):
                    if table[x+n][y] != 0:
                        table[x][y], table[x+n][y] = table[x+n][y], table[x][y]
                        break

    # 위쪽에서 교착상태 찾기
    for y in range(N):
        for x in range(N):
            if table[x][y] == 1 and table[x+1][y] == 2:
                deadlock += 1
    print('#{} {}'.format(tc+1, deadlock))
