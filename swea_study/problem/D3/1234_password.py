T = 10
for tc in range(1, T+1):
    N, S = input().split()
    N = int(N)
    code = list(S)
    password = []
    for i in range(N):
        if password == []:
            password.append(code[i])
        elif password != [] and password[-1] == code[i]:
            password.pop()
        else:
            password.append(code[i])

    print('#{} '.format(tc),end='')
    print(''.join(password))