T = int(input())
for tc in range(T):
    N = int(input())
    digit = [0]*10
    n = 1
    while digit != [1]*10:
        num = list(str(N * n))
        for i in range(len(num)):
            digit[int(num[i])] = 1
        n += 1
    print('#{} {}'.format(tc+1, N*(n-1)))