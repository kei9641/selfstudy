n = int(input())
line = 0
for i in range((n * 2 - 1), 2, -2):
    print(' ' * line + '*' * i)
    line += 1
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (i * 2 -1))