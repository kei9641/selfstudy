T = int(input())
for tc in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    sell = 0
    buy = 0
    for i in range(N-1, -1, -1):
        if buy > prices[i]:
            sell += buy - prices[i]
        else:
            buy = prices[i]
            
    print('#{} {}'.format(tc+1, sell))
            