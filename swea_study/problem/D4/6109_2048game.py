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
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if S == 'up':
        moveX = dx[0]
        moveY = dy[0] 
        # S 방향으로 정렬
        for y in range(N):
            for x in range(N): 
                if tile[x][y] == 0: # 기준값이 0
                    for n in range(1, N-x): # n칸 이동
                        if tile[x+moveX*n][y+moveY*n] != 0:
                            tile[x][y], tile[x+moveX*n][y+moveY*n] = tile[x+moveX*n][y+moveY*n], tile[x][y]
                            break
                        
        for y in range(N):
            for x in range(N):
                if isWall(x+moveX, y+moveY) == False:
                    if tile[x][y] == tile[x+moveX][y+moveY]:
                        tile[x][y] *= 2
                        for n in range(1, N-x-1): # n칸 이동
                            tile[x+moveX*n][y+moveY*n] = tile[x+moveX*(n+1)][y+moveY*(n+1)]
                        tile[N-1][y] = 0

    elif S == 'down':
        moveX = dx[1]
        moveY = dy[1] 
        # S 방향으로 정렬
        for y in range(N):
            for x in range(N-1, -1, -1): 
                if tile[x][y] == 0: # 기준값이 0
                    for n in range(1, x+1): # n칸 이동
                        if tile[x+moveX*n][y+moveY*n] != 0:
                            tile[x][y], tile[x+moveX*n][y+moveY*n] = tile[x+moveX*n][y+moveY*n], tile[x][y]
                            break

        for y in range(N):
            for x in range(N-1, -1, -1):
                if isWall(x+moveX, y+moveY) == False:
                    if tile[x][y] == tile[x+moveX][y+moveY]:
                        tile[x][y] *= 2
                        for n in range(1, x): # n칸 이동
                            tile[x+moveX*n][y+moveY*n] = tile[x+moveX*(n+1)][y+moveY*(n+1)]
                        tile[0][y] = 0

    elif S == 'left':
        moveX = dx[2]
        moveY = dy[2] 
        # S 방향으로 정렬
        for x in range(N):
            for y in range(N): 
                if tile[x][y] == 0: # 기준값이 0
                    for n in range(1, N-y): # n칸 이동
                        if tile[x+moveX*n][y+moveY*n] != 0:
                            tile[x][y], tile[x+moveX*n][y+moveY*n] = tile[x+moveX*n][y+moveY*n], tile[x][y]
                            break

        for x in range(N):
            for y in range(N):
                if isWall(x+moveX, y+moveY) == False:
                    if tile[x][y] == tile[x+moveX][y+moveY]:
                        tile[x][y] *= 2
                        for n in range(1, N-y-1): # n칸 이동
                            tile[x+moveX*n][y+moveY*n] = tile[x+moveX*(n+1)][y+moveY*(n+1)]
                        tile[x][N-1] = 0

    elif S == 'right':
        moveX = dx[3]
        moveY = dy[3] 
        # S 방향으로 정렬
        for x in range(N):
            for y in range(N-1, -1, -1): 
                if tile[x][y] == 0: # 기준값이 0
                    for n in range(1, y+1): # n칸 이동
                        if tile[x+moveX*n][y+moveY*n] != 0:
                            tile[x][y], tile[x+moveX*n][y+moveY*n] = tile[x+moveX*n][y+moveY*n], tile[x][y]
                            break

        for x in range(N):
            for y in range(N-1, -1, -1):
                if isWall(x+moveX, y+moveY) == False:
                    if tile[x][y] == tile[x+moveX][y+moveY]:
                        tile[x][y] *= 2
                        for n in range(1, y): # n칸 이동
                            tile[x+moveX*n][y+moveY*n] = tile[x+moveX*(n+1)][y+moveY*(n+1)]
                        tile[x][0] = 0

    print('#{}'.format(tc+1))
    for i in range(N):
        print(*tile[i])