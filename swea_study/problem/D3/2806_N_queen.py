dx = [1, 1, 1]
dy = [0, 1, -1]

def queen(x, k):
    global case
    if x == k:
        case += 1
        return
    for y in range(N):
        if board[x][y] == 0:
            board[x][y] = x+1
            for i in range(3):
                for n in range(1, N):
                    if not (0 <= x+dx[i]*n < N and 0 <= y+dy[i]*n < N):
                        break
                    if board[x+dx[i]*n][y+dy[i]*n] == 0:
                        board[x+dx[i]*n][y+dy[i]*n] = x+1
            queen(x+1, k)
            for x0 in range(N):
                for y0 in range(N):
                    if board[x0][y0] == x+1:
                        board[x0][y0] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    pre = [[0 for _ in range(N)] for _ in range(N)]
    case = 0
    queen(0, N)
    print('#{} {}'.format(tc, case))

# 이전 배열 값이 필요한 경우가 있음(순서를 표시한다면 해결 가능/복사를 잘 익히거나..)