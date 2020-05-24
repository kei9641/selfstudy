dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def isNotWall(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

def group(x0, y0):
    global cnt
    shape[x0][y0] = num
    if size[num] < cnt:
        size[num] = cnt
    for n in range(4):
        xn, yn = x0+dx[n], y0+dy[n]
        if isNotWall(xn, yn):
            if arr[xn][yn] and shape[xn][yn] == 0:
                cnt += 1
                group(xn, yn)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
shape = [[0 for _ in range(M)] for _ in range(N)]
size = [0 for _ in range(N*M//2+2)]
num = 1
result = 0
for x in range(N):
    for y in range(M):
        if arr[x][y] and shape[x][y] == 0:
            cnt = 1
            group(x, y)
            num += 1
if size.count(0) == (N*M//2+1):
    result = sum(size)
else:
    for x in range(N):
        for y in range(M):
            if shape[x][y] == 0:
                neighbor = []
                connect = 0
                for n in range(4):
                    xn, yn = x+dx[n], y+dy[n]
                    if isNotWall(xn, yn) and shape[xn][yn]:
                        if shape[xn][yn] not in neighbor:
                            neighbor.append(shape[xn][yn])
                            connect += size[shape[xn][yn]]
                if result < connect:
                    result = connect
    result += 1
print(result)
