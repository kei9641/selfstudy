T = int(input())
for tc in range(T):
    N = int(input())
    salary = 0
    for _ in range(N):
        p, x = map(float, input().split())
        salary += p * x
    print('#{0} {1:.6f}'.format(tc+1, salary))