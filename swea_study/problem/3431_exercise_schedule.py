T = int(input())
for tc in range(T):
    L, U, X = map(int, input().split())
    if L <= X <= U:
        print('#{} 0'.format(tc+1))
    elif X < L:
        print('#{} {}'.format(tc+1, L-X))
    elif U < X:
        print('#{} -1'.format(tc+1))