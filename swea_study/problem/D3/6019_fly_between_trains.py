T = int(input())
for tc in range(T):
    D, A, B, F = map(int, input().split())
    hour = D/(A+B)
    print('#{0} {1:.6f}'.format(tc+1, F*hour)) 