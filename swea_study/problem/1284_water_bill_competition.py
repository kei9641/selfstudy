T = int(input())
for tc in range(T):
    P, Q, R, S, W = map(int, input().split())
    chargeA = P * W
    if W <= R:
        chargeB = Q
    else:
        chargeB = Q + (W-R) * S
    if chargeA < chargeB:
        print('#{} {}'.format(tc+1, chargeA))
    else:
        print('#{} {}'.format(tc+1, chargeB))        