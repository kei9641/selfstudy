def cal(n, k, r, add, sub, mul, div):
    global minNum, maxNum
    if n==k:
        if maxNum < r:
            maxNum = r
        if minNum > r:
            minNum = r
    else:
        if add > 0:
            cal(n+1, k, r+card[n], add-1, sub, mul, div)
        if sub > 0:
            cal(n+1, k, r-card[n], add, sub-1, mul, div)
        if mul > 0:
            cal(n+1, k, r*card[n], add, sub, mul-1, div)
        if div > 0:
            cal(n+1, k, int(r/card[n]), add, sub, mul, div-1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    add, sub, mul, div = map(int, input().split())
    card = list(map(int, input().split()))
    minNum = 10**8
    maxNum = -10**8
    cal(1, N, card[0], add, sub, mul, div)
    print('#{} {}'.format(tc, maxNum-minNum))