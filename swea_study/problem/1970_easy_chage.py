T = int(input())
for tc in range(T):
    N = int(input())
    money = {
        50000 : 0,
        10000 : 0,
        5000 : 0,
        1000 : 0,
        500 : 0,
        100 : 0,
        50 : 0,
        10 : 0
    }
    for change in money.keys():
        while N >= change:
            N -= change
            money[change] += 1
    print('#{}'.format(tc+1))
    for i in money.values():
        print(i, end=' ')
    print()