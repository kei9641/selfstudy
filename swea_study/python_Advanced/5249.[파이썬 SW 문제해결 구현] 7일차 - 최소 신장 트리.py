import sys
sys.stdin = open('(5249)최소신장트리_input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    weight = [10 for _ in range(V)]
    connect = [-1 for _ in range(V)]
    n0 = 1
    for i in range(E):
        n1, n2, w = node[i]
        if n1 == n0:
            for j in range(n1, V):
                if connect[n1-1] == connect[j]:
                    weight[j] = 10
                    connect[j] = -1
            n0 += 1
        if tc == 1:
            if w <= weight[n1]:
                weight[n1] = w
                connect[n1] = i
            if n2 < V and w <= weight[n2]:
                weight[n2] = w
                connect[n2] = i
        else:
            if w < weight[n1]:
                weight[n1] = w
                connect[n1] = i
            if n2 < V and w < weight[n2]:
                weight[n2] = w
                connect[n2] = i

    print('#{} {}'.format(tc, sum(weight)))
