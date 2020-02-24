T = int(input())
for tc in range(T):
    audience = list(map(int, input()))
    clap = 0
    employee = 0
    for i in range(len(audience)):
        if i > clap and audience[i] != 0:
            employee += i - clap
            clap += i - clap + audience[i]
        else:
            clap += audience[i]
    print('#{} {}'.format(tc+1, employee))