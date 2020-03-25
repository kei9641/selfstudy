import sys
sys.stdin = open('그래프경로.txt')

def dfs(v):
    global ans

    visited[v] = 1
    for w in range(V+1):
        if gate[v][w] == 1 and visited[w] == 0:
            if w == G:
                ans = 1
            dfs(w)

T = int(input())
for tc in range(T):
    ans = 0
    V, E = map(int, input().split())
    gate = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        gate[start][end] = 1
    S, G = map(int, input().split())
    dfs(S)
    print('#{} {}'.format(tc+1, ans))