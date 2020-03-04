def connect(n, k, a, b, c, d):
    global result
    if n == k:
        result = ''.join(binary)
        return
    for i in range(2):
        binary[n] = str(i)
        if a > 0 and binary[n-1]+binary[n] == '00':
            connect(n+1, k, a-1, b, c, d)
        elif b > 0 and binary[n-1]+binary[n] == '01':
            connect(n+1, k, a, b-1, c, d)
        elif c > 0 and binary[n-1]+binary[n] == '10':
            connect(n+1, k, a, b, c-1, d)
        elif d > 0 and binary[n-1]+binary[n] == '11':
            connect(n+1, k, a, b, c, d-1)

T = int(input())
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    N = A+B+C+D+1
    binary = [0] * N
    result = ''
    for i in range(2):
        binary[0] = str(i)
        connect(1, N, A, B, C, D)
    print('#{}'.format(tc), end=' ')
    if len(result) == N:
        print(''.join(result))
    else:
        print('impossible')
'''
6
2 2 2 1
0 1 0 0
1 0 0 1
1 1 1 1
2 1 1 2
1 2 3 4
'''