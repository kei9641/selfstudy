num1, num2 = map(int, input().split())
for mul in range(1, 10):
    if num1 > num2:
        for dan in range(num1, num2-1, -1):
            print('{:<2}*{:^3}={:>3}'.format(dan, mul, dan*mul), end='   ')
    else:
        for dan in range(num1, num2+1):
            print('{:<2}*{:^3}={:>3}'.format(dan, mul, dan*mul), end='   ')
    print()