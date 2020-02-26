prime = []
for num in range(2, 1000):
    divisor = 0
    for n in range(2, 1000):
        if num == n: 
            if divisor == 0:
                prime.append(num)
            break
        if num % n == 0:
            divisor += 1

T = int(input())
for tc in range(T):
    N = int(input())
    duple = 0
    find_prime = 0
    for i in range(len(prime)):
        for j in range(i, len(prime)):
            for k in range(j, len(prime)):
                if prime[i]+prime[j]+prime[k] == N:
                    find_prime += 1
                if prime[i]+prime[j]+prime[k] >= N:
                    break
    print('#{} {}'.format(tc+1, find_prime))
