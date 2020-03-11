T = int(input())
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    result = ''
    if B == 0 and C == 0:
        if A == 0 and D != 0:
            result = '1'*(D+1)
        elif A != 0 and D == 0:
            result = '0'*(A+1)
        else:
            result = 'impossible'
    elif abs(B - C) > 1:
        result = 'impossible'
    elif B > C:
        result += '0'*(A+1)+'1'*(D+1)+'01'*C
    elif B < C:
        result += '1'*(D+1)+'0'*(A+1)+'10'*B
    elif B == C:
        result += '1'*(D+1)+'0'*(A+1)+'10'*(B-1)+'1'
    print('#{} {}'.format(tc, result))