from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global goal
    while q:
        x, y = q.popleft()
        for n in range(4):
            xn, yn = x+dx[n], y+dy[n]
            # 인덱스 범위 안이고
            if 0 <= xn < 100 and 0 <= yn < 100:
                # 방문한 적이 없으면
                if visited[xn][yn] == 0:
                    # 도착지이면
                    if maze[xn][yn] == 3:
                        goal = 1
                        return
                    # 길이면
                    elif maze[xn][yn] == 0:
                        visited[xn][yn] = 1
                        q.append((xn, yn))

for _ in range(10):
    tc = int(input())
    q = deque()
    maze = [list(map(int, input())) for _ in range(100)]
    visited = [[0 for _ in range(100)] for _ in range(100)]
    goal = 0
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1
                bfs()
    print('#{} {}'.format(tc, goal))