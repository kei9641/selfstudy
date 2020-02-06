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

        for i in range(8):
            while isWall(x-1 + dx[i], y-1 + dy[i]) == False: # 주변이 벽이 아니면
                if turn == 1: # 흑돌이면
                    if board[x-1 + dx[i]][y-1 + dy[i]] == 2: # 주변에 백돌이 있으면 방향 끝 값으로 이동
                        move = i
                        if i == 0:
                            start = 0
                            end = 0
                        elif i == 1:
                            start = 0
                            end = y-1
                        elif i == 2:
                            start = 0
                            end = N-1
                        elif i == 3:
                            start = x-1
                            end = N-1
                        elif i == 4:
                            start = N-1
                            end = N-1
                        elif i == 5:
                            start = N-1
                            end = y-1
                        elif i == 6:
                            start = 0
                            end = N-1
                        elif i == 7:
                            start = x-1
                            end = 0
                    break
                else: # 백돌이면
                    if board[x-1 + dx[i]][y-1 + dy[i]] == 1: # 주변에 흑돌이 있으면 방향 끝 값으로 이동
                        move = i
                        if i == 0:
                            start = 0
                            end = 0
                        elif i == 1:
                            start = 0
                            end = y-1
                        elif i == 2:
                            start = 0
                            end = N-1
                        elif i == 3:
                            start = x-1
                            end = N-1
                        elif i == 4:
                            start = N-1
                            end = N-1
                        elif i == 5:
                            start = N-1
                            end = y-1
                        elif i == 6:
                            start = 0
                            end = N-1
                        elif i == 7:
                            start = x-1
                            end = 0
                    break
        i = 0
        # while (x-1 != start - dx[move] * i) or (y-1 != end - dy[move] * i):
        #     if ((board[start - dx[move] * i][end - dy[move] * i] == turn) and (isWall(start - dx[move] * i, end - dy[move] * i) == False)):
        #         break
        #     i += 1
        for _ in range(N):
            if ((board[start - dx[move] * i][end - dy[move] * i] == turn) and (isWall(start - dx[move] * i, end - dy[move] * i) == False)):
                if board[start - dx[move] * i][end - dy[move] * i] == turn:
                    board[start - dx[move] * i][end - dy[move] * i] = turn
                    i += 1
            # print(i)

        board[x-1][y-1] = turn


        # moveX = 1
        # moveY = 1
        # for i in range(8):
        #     while isWall(x-1 + dx[i] * moveX, y-1 + dy[i] * moveY) == False:
        #         if turn == 1:
        #             if board[x-1 + dx[i]][y-1 + dy[i]] == 2:
                        
        #                 if board[x-1 + dx[i] + dx[i]][y-1 + dy[i] + dy[i]] == 1:
        #                     board[x-1 + dx[i]][y-1 + dy[i]] = 1
        #                     board[x-1][y-1] = 1
        #                 else:
                            
        #             break

        #         elif turn == 2:
        #             if board[x-1 + dx[i]][y-1 + dy[i]] == 1:
        #                 if board[x-1 + dx[i] + dx[i]][y-1 + dy[i] + dy[i]] == 2:
        #                     board[x-1 + dx[i]][y-1 + dy[i]] = 2
        #                     board[x-1][y-1] = 2
        #             break

        for i in range(len(board)):
            print(*board[i])
        print()


