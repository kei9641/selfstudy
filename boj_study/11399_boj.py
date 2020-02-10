N = int(input())
P = list(map(int, input().split()))
P.sort()
sumWithdrawal = 0
for i in range(N):
    sumWithdrawal += P[i] * (N-i)
print(sumWithdrawal)

