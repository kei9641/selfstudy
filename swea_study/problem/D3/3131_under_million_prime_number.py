N = 10**6+1
sieve = [True]*N
m = int(N**0.5)
for i in range(2, m+1):
    if sieve[i] == True:
        for j in range(i+i, N, i):
            sieve[j] = False
for i in range(2, N):
    if sieve[i] == True:
        print(i, end=' ')

# 소수 구할 때는 "에라토스테네스의 체" 