num1, num2 = map(int, input().split())
check1 = bool(num1 != 0)
check2 = bool(num2 != 0)
logicSquare = check1 and check2
logicSum = check1 or check2
print('{} {}'.format(int(logicSquare), int(logicSum)))