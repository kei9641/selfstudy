T = 10
for tc in range(1, T+1):
    N = int(input())
    formula = input()
    result = 0
    for i in range(N):
        if formula[i] != '+':
            result += int(formula[i])
    print('#{} {}'.format(tc, result))