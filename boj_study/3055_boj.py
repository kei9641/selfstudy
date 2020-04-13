dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def isNotWall(x,y):
    return (0 <= x < R) and (0 <= y < C)

def flood(x, y, t):
    print(x, y, forest[x][y])
    if forest[x][y] < t:
        return
    forest[x][y] = t
    for n in range(4):
        if isNotWall(x+dx[n], y+dy[n]):
            if type(forest[x+dx[n]][y+dy[n]]) == int:
                flood(x+dx[n], y+dy[n], t+1)

def escape(x, y, t):
    global result
    visited[x][y] = 1
    if forest[x][y] == 'D':
        result = t
        return
    for n in range(4):
        if isNotWall(x+dx[n], y+dy[n]):
            if forest[x+dx[n]][y+dy[n]] != 'X':
                if forest[x+dx[n]][y+dy[n]] > t+1:
                    escape(x+dx[n], y+dy[n], t+1)
                

R, C = map(int, input().split())
forest = []
for _ in range(R):
    forest.append(list(input()))

# 고슴도치가 이동한 경로
visited = [[0 for _ in range(C)] for _ in range(R)]

water = [] # 초기 물 위치
for x in range(R):
    for y in range(C):
        if forest[x][y] == 'S':
            Sx = x
            Sy = y
        elif forest[x][y] == '*':
            water.append(x)
            water.append(y)
            forest[x][y] = 0
        elif forest[x][y] == '.':
            forest[x][y] = 2500

for i in range(0, len(water), 2):
    flood(water[i], water[i+1], 0)

# print(forest)

result = 'KAKTUS'
escape(Sx, Sy, 0)
print(result)