import sys
sys.stdin = open('컨테이너_운반(5201).txt')

def dfs(v):
    global weigh
    if v == N:
        return
    for i in range(len(t)):
        if w[v] <= t[i] and visited[i] == 0:
            visited[i] = 1
            weigh += w[v]
            break
    dfs(v+1)


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    weigh = 0
    visited = [0 for _ in range(M)]
    dfs(0)
    print('#{} {}'.format(tc+1, weigh))
    
