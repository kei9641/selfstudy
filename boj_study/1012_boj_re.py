# organic cabbage
'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6

10 10 1
5 5
'''
def isWall(x, y):
    if 0 <= x < M and 0 <= y < N:
        return False
    return True

def dfs(x, y):
    global cnt
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited[x][y] = 1
    for n in range(4):
        if visited[x+dx[n]][y+dy[n]] == 1 and isWall(x+dx[n], y+dy[n]) == False:
            break
        else:
            cnt += 1
    for m in range(4):
        if visited[x+dx[m]][y+dy[m]] == 0 and ground[x+dx[m]][y+dy[m]]:
            dfs(x+dx[m], y+dy[m])

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    ground = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1
    
    for x in range(M):
        for y in range(N):
            if ground[y][x] == 1:
                x0, y0 = x, y
                break
    dfs(x0, y0)
    print(cnt)

