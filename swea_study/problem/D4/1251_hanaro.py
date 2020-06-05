import heapq
INF = float('inf')

def prim(n):
    tax = 0
    key[n] = 0
    heapq.heappush(preq, (key[n], 0))
    while preq:
        value, node = heapq.heappop(preq)
        if visited[node]:
            continue
        visited[node] = 1
        tax += value * E
        for i in range(N):
            if visited[i] == 0 and key[i] > length[node][i]:
                key[i] = length[node][i]
                # pi[i] = node
                heapq.heappush(preq, (key[i], i))
    return tax

T = int(input())
for tc in range(1, T+1):    
    preq = []
    N = int(input())
    xarr = list(map(int, input().split()))
    yarr = list(map(int, input().split()))
    E = float(input())
    length = [[0 for _ in range(N)] for _ in range(N)]
    visited = [0 for _ in range(N)]
    key = [INF for _ in range(N)]
    # pi = list(range(N))
    for i in range(N-1):
        for j in range(i+1, N):
            L = ((xarr[i]-xarr[j])**2 + (yarr[i]-yarr[j])**2)
            length[i][j] = L
            length[j][i] = L
    print('#%d %.f'%(tc, prim(0)))
