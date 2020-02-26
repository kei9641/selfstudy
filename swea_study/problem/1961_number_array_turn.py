T = int(input())
for tc in range(T):
    numbers = []
    N = int(input())
    for _ in range(N):
        numbers.append(list(map(int, input().split())))
    turn90 = [[0]*N for _ in range(N)]
    turn180 = [[0]*N for _ in range(N)]
    turn270 = [[0]*N for _ in range(N)]
    turnNum = [['']*3 for _ in range(N)]
    for x in range(N):
        for y in range(N):
            turn90[y][x] = numbers[N-1-x][y]
            turn180[x][y] = numbers[N-1-x][N-1-y]
            turn270[y][x] = numbers[x][N-1-y]
    for y0 in range(N):
        for x0 in range(N):
            turnNum[x0][0] += str(turn90[x0][y0])
            turnNum[x0][1] += str(turn180[x0][y0])
            turnNum[x0][2] += str(turn270[x0][y0])
    print('#{}'.format(tc+1))
    for i in range(N):
        print(*turnNum[i])