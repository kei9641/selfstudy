T = int(input())
for tc in range(T):
    n, h = input().split()
    N = int(n)
    numHex = int(h, 16)
    print('#{}'.format(tc+1),end=' ')
    print('{0:b}'.format(numHex).zfill(N*4))