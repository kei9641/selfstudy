N = int(input())
area = [[0]*101 for _ in range(101)]
for tc in range(N):
    y, x, column, row = map(int, input().split())
    for i in range(x, x+row):
        for j in range(y, y+column):
            area[i][j] = tc+1
cntArea = [0] * N
for n in range(1, N+1):
    for x in range(101):
        for y in range(101):
            if area[x][y] == n:
                cntArea[n-1] += 1
for i in range(len(cntArea)):
    print(cntArea[i])