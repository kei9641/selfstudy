import sys
sys.stdin = open("(5521)상원이의생일파티_input.txt")
T = int(input())

def bfs(v):
    global f, r

    r += 1
    Q[r] = v   #enQueue
    visit[v] = 1

    while (f != r):  #Not Empty
        f += 1
        v = Q[f]    #deQueue
        if visit[v] > 3: return

        for i in range(N+1):
            if G[v][i] and not visit[i]:
                r += 1
                Q[r] = i
                visit[i] = visit[v] + 1

for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = [[0 for _ in range(N+1)] for _ in range(N+1)]   #인접정점의 배열
    ans = 0
    Q = [0] * (N*N)
    f = -1
    r = -1
    visit = [0] * (N+1)

    for i in range(M):
        u, v = map(int, input().split())
        G[u][v] = G[v][u] = 1

    bfs(1)

    for i in range(N+1):
        if visit[i] == 2 or visit[i] == 3:
            ans += 1

    print("#{} {}".format(tc, ans))