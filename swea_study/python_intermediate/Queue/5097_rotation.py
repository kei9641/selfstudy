T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))
    idx = M % N
    print('#{} {}'.format(tc, number[idx]))