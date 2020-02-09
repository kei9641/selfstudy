import sys
sys.stdin = open('othello.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    # 초기 돌 셋팅
    board[int(N/2-1)][int(N/2-1)] = 2
    board[int(N/2)][int(N/2)] = 2
    board[int(N/2-1)][int(N/2)] = 1
    board[int(N/2)][int(N/2-1)] = 1

    Blackcnt = 0
    Whitecnt = 0

    def isWall(x, y):
        if 0 <= x < N and 0 <= y < N: # 벽을 만나면 True
            return False
        return True

    for _ in range(M):
        x, y, turn = map(int, input().split())
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]

        if turn == 1:
            for i in range(8):
                if isWall(x-1+dx[i],y-1+dy[i]) == False and board[x-1+dx[i]][y-1+dy[i]] == 2:
                    moveN = 0
                    moveX = dx[i]
                    moveY = dy[i]
                    for n in range(1, N):
                        if isWall(x-1+moveX*n,y-1+moveY*n) == False:
                            if board[x-1+moveX*n][y-1+moveY*n] == 1:
                                moveN = n
                                break
                    for n in range(moveN):
                        if isWall(x-1+moveX*n,y-1+moveY*n) == False:
                            board[x-1+moveX*n][y-1+moveY*n] = 1
        
        elif turn == 2:
            for i in range(8):
                if isWall(x-1+dx[i],y-1+dy[i]) == False and board[x-1+dx[i]][y-1+dy[i]] == 1:
                    moveN = 0
                    moveX = dx[i]
                    moveY = dy[i]
                    for n in range(1, N):
                        if isWall(x-1+moveX*n,y-1+moveY*n) == False:
                            if board[x-1+moveX*n][y-1+moveY*n] == 2:
                                moveN = n
                                break
                    for n in range(moveN):
                        if isWall(x-1+moveX*n,y-1+moveY*n) == False:
                            board[x-1+moveX*n][y-1+moveY*n] = 2

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                Blackcnt += 1
            elif board[i][j] == 2:
                Whitecnt += 1
    print('#{} {} {}'.format(tc+1, Blackcnt, Whitecnt))