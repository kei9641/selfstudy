def findG():
    for i in range(V-1):
        for j in depth[i]:
            visited[j] = 1
            for n in node[j]:
                if visited[n] == 0:
                    depth[i+1].append(n)
                    if n == G:
                        return

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
    depth = [[] for _ in range(V)]
    depth[0].append(S)
    result = 0
    findG()
    for i in range(len(depth)):
        if G in depth[i]:
            result = i
    print('#{} {}'.format(tc, result))
