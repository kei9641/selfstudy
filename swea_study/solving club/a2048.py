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
                        if isWall(x+moveX*n, y+moveY*n) == False:
                            if tile[x+moveX*n][y+moveY*n] != 0: # n번 이동한 곳에 값이 있으면
                                tile[x][y], tile[x+moveX*n][y+moveY*n] = tile[x+moveX*n][y+moveY*n], tile[x][y]

        for y in range(N):
            for x in range(N):
                if isWall(x+moveX, y+moveY) == False:
                    if tile[x][y] == tile[x+moveX][y+moveY]:
                        tile[x][y] *= 2
                        tile[x+moveX][y+moveY] = 0
                        for n in range(2, N-x): # n칸 이동
                            if isWall(x+moveX*n, y+moveY*n) == False:
                                if tile[x+moveX*n][y+moveY*n] != 0: # n번 이동한 곳에 값이 있으면
                                    tile[x+moveX][y+moveY], tile[x+moveX*n][y+moveY*n] = tile[x+moveX*n][y+moveY*n], tile[x+moveX][y+moveY]
                                    for i in range(N):
                                        print(*tile[i])
                                    print()
    