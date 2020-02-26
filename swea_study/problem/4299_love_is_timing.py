T = int(input())
for tc in range(T):
    D, H, M = map(int, input().split())
    baseD = 11
    baseH = 11
    baseM = 11
    H += (D - baseD) * 24
    M += (H - baseH) * 60
    wait = M - baseM
    if wait < 0:
        print('#{} -1'.format(tc+1))
    else:
        print('#{} {}'.format(tc+1, wait))