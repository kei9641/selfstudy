num1, num2 = map(int, input().split())
num1 += 100
num2 %= 10
print('{} {}'.format(num1, num2))