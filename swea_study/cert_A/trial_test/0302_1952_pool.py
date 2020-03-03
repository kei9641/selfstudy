def membership(n, s, d, m, th):
    global fee
    if n > 12:
        if fee > s:
            fee = s
    elif fee <= s:
        return
    else:
        membership(n+1, s+min(plan[n]*d, m), d, m, th)
        membership(n+3, s+th, d, m, th)
    

T = int(input())
for tc in range(1, T+1):
    D, M, Th, Y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    fee = Y
    membership(1, 0, D, M, Th)
    print('#{} {}'.format(tc, fee))