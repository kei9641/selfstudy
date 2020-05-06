T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    x,y, u,v = 0,1, 1,0
    print(A, B, x, y, u, v)
    while A != 0:
        q, r = B//A, B%A
        m, n = x-u*q, y-v*q
        B,A, x,y, u,v = A,r, u,v, m,n
        print(A, B, x, y, u, v)
    gcd = B
    if gcd == 1:
        print('#{} {} {}'.format(tc, x, y))
    else:
        print('#{} -1'.format(tc))
