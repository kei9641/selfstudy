

T = int(input())
for tc in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    benefit = 0
    sell = []
    for i in range(1, N):
        if prices[i-1] <= prices[i]:
            sell.append(prices[i-1])
        else:
            for j in range(len(sell)):
                benefit += prices[i] - sell[j]
                
            sell.clear()
    print(benefit)
            


'''
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2   
'''