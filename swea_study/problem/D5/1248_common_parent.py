import sys
sys.stdin = open('q.txt')

T = int(input())
for tc in range(1, T+1):
    V, E, A, B = map(int, input().split())
    connect = list(map(int, input().split()))
    node = [[0 for _ in range(3)] for _ in range(V+1)]
    for i in range(0, len(connect), 2):
        if node[connect[i]][0]:
            node[connect[i]][1] = connect[i+1]
        else:
            node[connect[i]][0] = connect[i+1]
        node[connect[i+1]][2] = connect[i]
    p = 0
    parrentA = [A]
    while node[A][2]:
        A = node[A][2]
        parrentA.append(A)
    while node[B][2]:
        B = node[B][2]
        if B in parrentA:
            p = B
            break
    sub = [p]
    idx = 0
    while idx < len(sub):
        if node[sub[idx]][0]:
            sub.append(node[sub[idx]][0])
        if node[sub[idx]][1]:
            sub.append(node[sub[idx]][1])
        idx += 1
    print('#{} {} {}'.format(tc, sub[0], idx))

