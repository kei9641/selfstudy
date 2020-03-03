def find_binary(n):
    global A, B, C, D, result, length
    
    if n == 2 ** (length):
        result = 'important'
        return
    binary = '{0:b}'.format(n).zfill(length)
    # print(A,B,C,D,binary,n, result)
    for i in range(1, length):
        if A > 0 and binary[i-1] + binary[i] == '00':
            A -= 1
            if A+B+C+D == 0:
                result = binary
                return
        elif B > 0 and binary[i-1] + binary[i] == '01':
            B -= 1
            if A+B+C+D == 0:
                result = binary
                return
        elif C > 0 and binary[i-1] + binary[i] == '10':
            C -= 1
            if A+B+C+D == 0:
                result = binary
                return
        elif D > 0 and binary[i-1] + binary[i] == '11':
            D -= 1
            if A+B+C+D == 0:
                result = binary
                return
        else:
            find_binary(n+1)

T = int(input())
for tc in range(T):
    A, B, C, D = map(int, input().split())
    length = A+B+C+D+1
    result = ''
    find_binary(0)
    print(result)