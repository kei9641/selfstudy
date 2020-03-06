T = int(input())
for tc in range(1, T+1):
    N ,A, B = map(int, input().split())
    n = int(N**0.5)
    minN = 2*(10**10)
    for RC in range(N, n**2-1, -1):
        for C in range(n, 0, -1):
            if RC % C == 0:
                R = RC // C
                break
        if A*abs(R-C)+B*(N-RC) < minN:
            minN = A*abs(R-C)+B*(N-RC)
    print('#{} {}'.format(tc, minN))
