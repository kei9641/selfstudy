T = int(input())
for tc in range(1, T+1):
    p, q = map(float, input().split())
    s1 = (1-p)*q
    s2 = p*(1-q)*q
    result = 'NO'
    if s1 < s2:
        result = 'YES'
    print('#{} {}'.format(tc, result))