dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def isWall(x, y):
    if 0 <= x < N and 0 <= y < N:
        return False
    return True

def turn(x0, y0, c, j):
    if isWall(x0+dx[j], y0+dy[j]) == True:
        return
    if board[x0+dx[j]][y0+dy[j]] != c and board[x0+dx[j]][y0+dy[j]] != 0:
        turn(x0+dx[j], y0+dy[j], c, j)
    if board[x0+dx[j]][y0+dy[j]] == c:
        board[x0][y0] = c
        return

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    play = []
    for _ in range(M):
        play.extend(list(map(int, input().split())))
    # 초기돌 세팅
    board[N//2][N//2] = 2
    board[N//2-1][N//2] = 1
    board[N//2-1][N//2-1] = 2
    board[N//2][N//2-1] = 1
    
    for i in range(0, M*3, 3):
        for j in range(8):
            turn(play[i+1]-1, play[i]-1, play[i+2], j)

    W = 0
    B = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:
                B += 1
            elif board[x][y] == 2:
                W += 1
    print('#{} {} {}'.format(tc+1, B, W))
