#        ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

sea = [[0 for _ in range(4)] for _ in range(4)]
vect = [[0 for _ in range(4)] for _ in range(4)]
fish = [[] for _ in range(17)]
case = []
for i in range(4):
    arr = list(map(int, input().split()))
    for j in range(8):
        if j % 2:
            vect[i][(j-1)//2] = arr[j]
        else: 
            sea[i][j//2] = arr[j]

shark = sea[0][0] # 상어가 먹은 물고기 합
sea[0][0] = -1 # (0, 0)에 상어 배치

# 물고기 위치 찾기
for i in range(4):
    for j in range(4):
        if sea[i][j] > 0:
            fish[sea[i][j]].append(i)
            fish[sea[i][j]].append(j)

# 물고기 이동
for n in range(1, 17):
    if fish[n] != []:
        x, y = fish[n]
        # 물고기가 이동할 때까지
        turn = 0
        while turn < 8:
            xn, yn = x+dx[vect[x][y]], y+dy[vect[x][y]]
            if 0 <= xn < 4 and 0 <= yn < 4:
                # 물고기가 이동할 칸에 상어가 있다면 방향 변경
                if sea[xn][yn] == -1:
                    vect[x][y] += 1
                # 물고기가 이동할 칸이 비어있거나 다른 물고기가 있다면 자리 교체
                else:
                    if sea[xn][yn]:
                        fish[n], fish[sea[xn][yn]] = fish[sea[xn][yn]], fish[n]
                    sea[x][y], sea[xn][yn] = sea[xn][yn], sea[x][y]
                    vect[x][y], vect[xn][yn] = vect[xn][yn], vect[x][y]
                    break

            # 물고기가 이동할 칸이 없다면 방향 변경
            else:
                vect[x][y] += 1

            turn += 1
            # 물고기가 이동할 수 없으면 원래 방향으로
            if turn == 7:
                vect[x][y] += 1
            # 방향 인덱스 값이 벗어나지 않도록
            if vect[x][y] > 8:
                vect[x][y] = 1
case.append([sea, vect, fish])

