T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = list(map(int, input().split()))
    result = 0
    for i in range(N):
        result += (S[i]//10)**(S[i]%10)
    print('#{} {}'.format(tc, result))
