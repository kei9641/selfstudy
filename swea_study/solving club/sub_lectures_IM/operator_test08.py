num1, num2, num3 = map(int, input().split())
if num1 > num2 and num1 > num3:
    result1 = 1
else:
    result1 = 0
if num1 == num2 == num3:
    result2 = 1
else:
    result2 = 0
print('{} {}'.format(result1, result2))