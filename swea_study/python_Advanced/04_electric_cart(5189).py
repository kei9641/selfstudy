import sys
sys.stdin = open('electric_cart.txt')

def dfs(v):
    global result, use
    visited[v] = 1
    if visited == [1] * N:
        use += field[v][0]
        if use < result:
            result = use
        use -= field[v][0]
        return
    for w in range(N):
        if v != w and visited[w] == 0:
            use += field[v][w]
            dfs(w)
            use -= field[v][w]
            visited[w] = 0
        
T = int(input())
for tc in range(T):
    N = int(input())
    field = []
    for _ in range(N):
        field.append(list(map(int, input().split())))
    visited = [0 for _ in range(N)]
    use = 0
    result = 987654321
    dfs(0)
    print('#{} {}'.format(tc+1, result))