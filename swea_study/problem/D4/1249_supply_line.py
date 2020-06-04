from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        x, y = q.popleft()
        for n in range(4):
            xn, yn = x+dx[n], y+dy[n]
            if 0 <= xn < N and 0 <= yn < N:
                if const[x][y]+road[xn][yn] < const[xn][yn]:
                    const[xn][yn] = const[x][y]+road[xn][yn]
                    q.append((xn, yn))

T = int(input())
for tc in range(1, T+1):
    q = deque()
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)]
    const = [[100000 for _ in range(N)] for _ in range(N)]
    const[0][0] = 0
    q.append((0, 0))
    bfs()
    print('#{} {}'.format(tc, const[-1][-1]))