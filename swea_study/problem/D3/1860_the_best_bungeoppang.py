T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    client = list(map(int, input().split()))
    bungeoppang = 0
    result = 'Possible' 
    for t in range(1, M*N+1):
        if t % M == 0:
            bungeoppang += K
        if t in client:
            bungeoppang -= 1
            if bungeoppang < 0:
                result = 'Impossible'
                break
    if 0 in client:
        result = 'Impossible'
    print('#{} {}'.format(tc, result))