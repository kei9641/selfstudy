T = int(input())
for tc in range(T):
    N = int(input())
    S1 = (1+N)*N//2
    S2 = N**2
    S3 = N**2+N
    print('#{} {} {} {}'.format(tc+1, S1, S2, S3))

# 규칙적으로 연속된 수의 합을 구할 때는 공식을 사용하는 것이 더 좋음