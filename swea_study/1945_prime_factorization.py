T = int(input())
for tc in range(T):
    N = int(input())
    factorizaion = []
    count = []
    prime = [2, 3, 5, 7, 11]
    def factor(n):
        if n == 1:
            return
        for num in range(2, n+1):
            if n % num == 0:
                factorizaion.append(num)
                factor(n//num)
                break
    factor(N)
    for i in range(5):
        count.append(factorizaion.count(prime[i]))
    print('#{}'.format(tc+1), end=' ')
    print(*count)
