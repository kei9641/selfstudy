def dfs(v):
    global V
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, V+1):
        if works[i][v] == 1:
            if works[i].count(1) == 1:
                if visited[i] == 0:
                    works[i][v] = 0
                    dfs(i)
            else:
                works[i][v] = 0

def start():
    global V
    for i in range(1, V+1):
        if works[i] == [0]*(V+1) and visited[i] == 0:
            dfs(i)
            
for tc in range(10):
    V, E = map(int, input().split())
    works = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    lines = list(map(int, input().split()))
    route = []

    for n in range(0, E*2, 2):
        works[lines[n+1]][lines[n]] = 1
    print('#{}'.format(tc+1), end=' ')

    start()
    if visited != [1]*(V+1):
        start()
    print()
