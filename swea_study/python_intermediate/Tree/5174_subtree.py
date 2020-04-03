T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    line = list(map(int, input().split()))
    graph = [[] for _ in range(E+2)]
    for i in range(0, E*2-1, 2):
        graph[line[i]].append(line[i+1])
    node = [N]
    idx = 0
    while idx != len(node):
        node.extend(graph[node[idx]])
        idx += 1
    print('#{} {}'.format(tc, len(node)))