T = int(input())
for tc in range(1, T+1):
    code = list(map(int, input().split()))
    decode = ['00', '01', '10', '11']
    N = sum(code)
    password = ['0']
    result = ''
    if N in code:
        if N == 1:
            password = list(decode[code.index(1)])
        else:
            if N == code[1] or N == code[2]:
                password = ['0']
            elif N == code[0]:
                password = ['0'] * (N+1)
            elif N == code[3]:
                password = ['1'] * (N+1)
    elif code[1] == code[2] == 0:
        password = ['0']
    else:
        if code[1] == code[2]:
            password += ['1', '0'] * code[2]
        elif code[1]+1 == code[2]:
            password += ['1', '0'] * code[1]
            password.insert(0, '1')
        elif code[1] == code[2]+1:
            password += ['1', '0'] * code[2]
            password.insert(len(password), '1')
        else:
            password = ['0']
        while code[0] != 0:
            password.insert(password.index('0'), '0')
            code[0] -= 1
        while code[3] != 0:
            password.insert(password.index('1'), '1')
            code[3] -= 1

    if len(password) == N+1:
        result = ''.join(password)
    else:
        result = 'impossible'
    print('#{} {}'.format(tc, result))
