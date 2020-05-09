divisor = [0 for _ in range(1000001)]

for i in range(1, 1000001, 2):
    for j in range(1, 1000000//i+1):
        divisor[i*j] += i            
for i in range(1, 1000001):
    divisor[i] += divisor[i - 1]

T = int(input())
for tc in range(1, T+1):
    L, R = map(int, input().split())
    result = divisor[R] - divisor[L-1]
    print('#{} {}'.format(tc, result))