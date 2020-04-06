T = 10
for tc in range(1, T+1):
    N = int(input())
    formula = list(input())
    calculate = []
    i = 0
    while i < N:
        if formula[i] == '*':
            formula[i], formula[i+1] = formula[i+1], formula[i]
            i += 2
        else:
            i += 1
    for j in range(N):
        if formula[j] == '+':
            formula.append(formula.pop(j))
    for n in formula:
        if n == '+':
            calculate.append(int(calculate.pop(-2)) + int(calculate.pop(-1)))
        elif n == '*':
            calculate.append(int(calculate.pop(-2)) * int(calculate.pop(-1)))
        else:
            calculate.append(n)
    print('#{} {}'.format(tc, calculate.pop()))