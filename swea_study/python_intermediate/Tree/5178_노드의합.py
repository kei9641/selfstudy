import sys
sys.stdin = open('노드의합.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    leaf = []
    for _ in range(M):
        idx, num = map(int, input().split())
        leaf.append(idx)
        tree[idx] = num
    for i in range(N, 0, -1):
        if i not in leaf:
            tree[i] = tree[i*2]
            if i*2 < N:
                tree[i] += tree[i*2+1]
    print('#{} {}'.format(tc, tree[L]))