T = int(input())
for tc in range(T):
    A, B, C = map(int, input().split())
    if A < B:
        print('#{} {}'.format(tc+1, C//A))
    else:
        print('#{} {}'.format(tc+1, C//B))