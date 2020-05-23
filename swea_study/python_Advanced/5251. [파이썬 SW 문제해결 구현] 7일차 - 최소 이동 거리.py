import sys
sys.stdin = open('(5251)최소이동거리_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    L = node[-1][1] + 1
    weight = [10000 for _ in range(L)]
    visit = [0 for _ in range(L)]
    n = 0
    weight[0] = 0
    visit[-1] = 2
    while visit != [2 for _ in range(L)]:
        visit[n] = 2
        for i in range(E):
            if node[i][0] == n:
                s, e, w = node[i]
                if weight[e] >= w + weight[s]:
                    weight[e] = w + weight[s]
                    visit[e] = 1
            elif node[i][0] > n:
                break
        m = 10000
        for j in range(1, L):
            if visit[j] == 1 and m > weight[j]:
                m = weight[j]
                n = j
    print('#{} {}'.format(tc, weight[N]))
