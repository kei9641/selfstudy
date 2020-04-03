T = int(input())
for tc in range(1, T+1):
    N = int(input())
    juice = '1/' + str(N)
    juice += (' ' + juice) * (N-1)
    print('#{} {}'.format(tc, juice))