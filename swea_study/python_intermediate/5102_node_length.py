T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    S, G = map(int, input().split())
    visited = [0 for _ in range(V+1)]
    route = []
    result = 0
    s = S
    while s != G:
        route.append(-1)
        for i in range(len(node[s])):
            route.append(node[s][i])
        if route[0] == -1:
            result += 1
            route.pop(0)
        else:
            visited[route[0]] = 1
            s = route[0]
            route.pop(0)
        print(route)
    print(result)
    # result = 0
    # if sum(node[S-1]) <= sum(node[G-1]):
    #     visited[S-1] = 1
    #     dfs(S-1, G-1, route)
    # else:
    #     visited[G-1] = 1
    #     dfs(G-1, S-1, route)
    # print('#{} {}'.format(tc, result))