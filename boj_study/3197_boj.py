'''
1. 2
2. 2,,
3. 6
4. 19
5. 584
6. 358
7. 99
8. 153
9. 89
10. 166
11. 224
12. 97
13. 4
14. 147
'''
# # import sys
# # sys.stdin = open('tc13.txt')
# # sys.setrecursionlimit(100000)

# from collections import deque

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def isNotWall(x, y):
#     return (0 <= x < R) and (0 <= y < C)

# def bfs(t):
#     global day
#     # print(t)
#     # if meltT < t:
#     #     return
#     while swan1:
#         x, y = swan1.popleft()
#         # print(x, y)
#         visited[x][y] = 1
#         for n in range(4):
#             if isNotWall(x+dx[n], y+dy[n]):
#                 if visited[x+dx[n]][y+dy[n]] == 2:
#                     day = t
#                     return
#                 if visited[x+dx[n]][y+dy[n]] == 0 and lake[x+dx[n]][y+dy[n]] <= t:
#                     swan1.append((x+dx[n], y+dy[n]))
#                     s1.append((x+dx[n], y+dy[n]))
#         # for i in range(R):
#         #     print(*visited[i])
#         # print()
#     # print('!!!!!!!!!!!!!!!!!!!!!!')
#     while swan2:
#         x, y = swan2.popleft()
#         visited[x][y] = 2
#         for n in range(4):
#             if isNotWall(x+dx[n], y+dy[n]):
#                 if visited[x+dx[n]][y+dy[n]] == 1:
#                     day = t
#                     return
#                 if visited[x+dx[n]][y+dy[n]] == 0 and lake[x+dx[n]][y+dy[n]] <= t:
#                     swan2.append((x+dx[n], y+dy[n]))
#                     s2.append((x+dx[n], y+dy[n]))
#         # for i in range(R):
#         #     print(*visited[i])
#         # print()
#     swan1.extend(s1)
#     swan2.extend(s2)
#     bfs(t+1)

# q = deque()
# R, C = map(int, input().split())
# lake = [list(input()) for _ in range(R)]
# swan1 = deque()
# swan2 = deque()
# s1 = []
# s2 = []
# visited = [[0 for _ in range(C)] for _ in range(R)]

# for x in range(R):
#     for y in range(C):
#         if lake[x][y] == '.':
#             lake[x][y] = 0
#             q.append((x, y))
#         elif lake[x][y] == 'L':
#             q.append((x, y))
#             lake[x][y] = 0
#             if swan1:
#                 swan2.append((x, y))
#             else:
#                 swan1.append((x, y))
#             visited[x][y] = 0

# while q:
#     x, y = q.popleft()
#     for n in range(4):
#         if isNotWall(x+dx[n], y+dy[n]):
#             if lake[x+dx[n]][y+dy[n]] == 'X':
#                 lake[x+dx[n]][y+dy[n]] = lake[x][y] + 1
#                 q.append((x+dx[n], y+dy[n]))
# # for i in range(R):
# #     print(*lake[i])
# # print()
# # meltT = lake[x][y]
# day = 0
# bfs(0)
# # print(day)
# # print(meltT)
# # print(swan1, swan2)




'''
- 얼음 녹이기(while)
1. '.' 물공간('L'포함)을 0 으로 바꾸고 queue에 저장, 
    'L'의 위치를 따로 저장, swan에 백조 위치 넣고 visited에 그 위치를 0
2. popleft로 사방을 확인하여 'X'이면 현재+1 하고 queue에 저장
- 백조 이동시키기(bfs)
3. queue가 비면 bfs 
4. popleft로 사방을 확인하여 lake의 숫자가 현재+1보다 작으면 visited에 현재+1
5. 사방 visited 숫자가 현재+1과 같으면 result에 저장후 종료
'''

from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not c[nx][ny]:
                    if lake[nx][ny] == '.':
                        q.append([nx, ny])
                    else:
                        q_temp.append([nx, ny])
                    c[nx][ny] = 1
    return 0

def melt():
    while water:
        x, y = water.popleft()
        if lake[x][y] == 'X':
            lake[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not wc[nx][ny]:
                    if lake[nx][ny] == 'X':
                        wq_temp.append([nx, ny])
                    else:
                        water.append([nx, ny])
                    wc[nx][ny] = 1

R, C = map(int, input().split())
lake = []
for _ in range(R):
    lake.append(list(input()))

c = [[0] * C for _ in range(R)]
wc = [[0] * C for _ in range(R)]


swan = []
q, q_temp, water, wq_temp = deque(), deque(), deque(), deque()


for i in range(R):
    for j in range(C):
        if lake[i][j] == 'L':
            swan.extend([i, j])
            water.append([i, j])
        elif lake[i][j] == '.':
            wc[i][j] = 1
            water.append([i, j])

x1, y1, x2, y2 = swan
q.append([x1, y1])
lake[x1][y1], lake[x2][y2], c[x1][y1] = '.', '.', 1
cnt = 0
for i in range(R):
    print(*wc[i])
while True:
    melt()
    if bfs():
        print(cnt)
        break
    q, water = q_temp, wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt += 1
