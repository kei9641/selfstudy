def squarMinus(n1, n2):
    return abs(n1**2 - n2**2)

num1, num2 = map(int, input().split())
print(squarMinus(num1, num2))