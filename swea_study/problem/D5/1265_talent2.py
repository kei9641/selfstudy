T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    num = N//P
    bundle = [num for _ in range(P)]
    remain = N - num*P
    i = 0
    while remain:
        bundle[i] += 1
        remain -= 1
        i += 1
        if i == P:
            i = 0
    candy = 1
    for n in range(P):
        candy *= bundle[n]
    print('#{} {}'.format(tc, candy))