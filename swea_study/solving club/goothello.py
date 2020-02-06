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

    def isWall(x, y):
        if 0 <= x < N and 0 <= y < N: # 벽을 만나면 True
            return False
        return True

    for _ in range(M):
        x, y, turn = map(int, input().split())
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        color = ''
        if turn == 1:
            while color != 'W':
                for i in range(8):
                    if isWall(x-1+dx[i]*2, y-1+dy[i]*2) == False:
                        if (board[(x-1)+dx[i]][(y-1)+dy[i]] == 2) and (board[(x-1)+dx[i]*2][(y-1)+dy[i]*2] == 1):
                            moveX = dx[i]
                            moveY = dy[i]
                            while color != 'B':
                                for j in range(N):
                                    if board[(x-1)+moveX*j][(y-1)+moveY*j] != 1:
                                        board[(x-1)+moveX*j][(y-1)+moveY*j] = 1
                                    else:
                                        color = 'B'
                                        break
                            if isWall(x-1+dx[i+1]*2, y-1+dy[i+1]*2) == False:
                                if (board[(x-1)+dx[i+1]][(y-1)+dy[i+1]] == 2) and (board[(x-1)+dx[i+1]*2][(y-1)+dy[i+1]*2] == 1): 
                                    continue
                                else:
                                    color = 'W'
                                    break
                            else:
                                break

        else:
            while color != 'B':
                for i in range(8):
                    if isWall(x-1+dx[i]*2, y-1+dy[i]*2) == False:
                        if (board[(x-1)+dx[i]][(y-1)+dy[i]] == 1) and (board[(x-1)+dx[i]*2][(y-1)+dy[i]*2] == 2):
                            moveX = dx[i]
                            moveY = dy[i]
                            while color != 'W':
                                for j in range(N):
                                    if board[(x-1)+moveX*j][(y-1)+moveY*j] != 2:
                                        board[(x-1)+moveX*j][(y-1)+moveY*j] = 2
                                    else:
                                        color = 'W'
                                        break
                            if isWall(x-1+dx[i+1]*2, y-1+dy[i+1]*2) == False:
                                if (board[(x-1)+dx[i+1]][(y-1)+dy[i+1]] == 1) and (board[(x-1)+dx[i+1]*2][(y-1)+dy[i+1]*2] == 2): 
                                    continue
                                else:
                                    color = 'B'
                                    break
                            else:
                                break


        for i in range(len(board)):
            print(*board[i])
        print()