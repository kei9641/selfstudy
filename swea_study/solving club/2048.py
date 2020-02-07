import sys
sys.stdin = open('2048.txt')

T = int(input())
for tc in range(T):
    a, S = input().split()
    N = int(a)
    tile = []
    for _ in range(N):
        tile.append(list(map(int, input().split())))

    def isWall(x, y):
        if 0 <= x < N and 0 <= y < N: # 벽을 만나면 True
            return False
        return True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # if S == 'down':
    #     moveX = dx[0]
    #     moveY = dy[0]
    #     for y in range(N):
    #         for x in range(N-1, 0, -1):
    #             if tile[x][y] == 0:
    #                 for n in range(N):
    #                     if tile[x+moveX*n][y+moveY*n] != 0:
    #                         tile[x][y], tile[x+moveX*n][y+moveY*n] = tile[x+moveX*n][y+moveY*n], tile[x][y]
    #                         break
    #             else:
    #                 if tile[x][y] == tile[x+moveX][y+moveY]:
    #                     tile[x][y] *= 2
    #                     tile[x+moveX][y+moveY] = 0

    if S == 'up':
        moveX = dx[1]
        moveY = dy[1] 
        for y in range(N):
            for x in range(N-1): 
                if tile[x][y] == 0: # 기준값이 0
                    for n in range(N): # n칸 이동
                        if isWall(x+moveX*n, y+moveY*n) == False:
                            if tile[x+moveX*n][y+moveY*n] != 0: # n번 이동한 곳에 값이 있으면 
                                #tile[x][y] = tile[x+moveX*n][y+moveY*n] # 기준에 n번 이동한 값을 입력
                                if isWall(x+moveX*(n+1), y+moveY*(n+1)) == False:
                                    if tile[x+moveX*n][y+moveY*n] == tile[x+moveX*(n+1)][y+moveY*(n+1)]: # 단, n번 이동한 값이 다음 값과 같다면
                                        tile[x][y] = tile[x+moveX*n][y+moveY*n] * 2 # 두배
                                        tile[x+moveX*n][y+moveY*n] = 0
                                        tile[x+moveX*(n+1)][y+moveY*(n+1)] = 0 
                                    else:
                                        tile[x+moveX*n][y+moveY*n] = 0
                                else:
                                        tile[x+moveX*n][y+moveY*n] = 0
                                break
                else:
                    if tile[x][y] == tile[x+moveX][y+moveY]:
                        tile[x][y] *= 2
                        tile[x+moveX][y+moveY] = 0
                    else: # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        

    # elif S == 'left':
    #     moveX = dx[2]
    #     moveY = dy[2]
    #     for x in range(N-1, -1, -1):
    #         for y in range(N-1):
    #             if tile[x][y] == 0:
    #                 for n in range(N):
    #                     if tile[x+moveX*n][y+moveY*n] != 0:
    #                         tile[x][y], tile[x+moveX*n][y+moveY*n] = tile[x+moveX*n][y+moveY*n], tile[x][y]
    #                         break
    #             else:
    #                 if tile[x][y] == tile[x+moveX][y+moveY]:
    #                     tile[x][y] *= 2
    #                     tile[x+moveX][y+moveY] = 0

    # elif S == 'right':
    #     moveX = dx[3]
    #     moveY = dy[3]
    #     for x in range(N):
    #         for y in range(N-1):
    #             if tile[x][y] == 0:
    #                 for n in range(N):
    #                     if tile[x+moveX*n][y+moveY*n] != 0:
    #                         tile[x][y], tile[x+moveX*n][y+moveY*n] = tile[x+moveX*n][y+moveY*n], tile[x][y]
    #                         break
    #             else:
    #                 if tile[x][y] == tile[x+moveX][y+moveY]:
    #                     tile[x][y] *= 2
    #                     tile[x+moveX][y+moveY] = 0
    for i in range(N):
        print(*tile[i])
    
    
