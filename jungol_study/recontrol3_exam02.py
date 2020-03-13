num = int(input())
for i in range(10):
    if (num * (i+1)) < 100:
        print(num * (i+1), end=' ')
    if (num * (i+1)) % 10 == 0:
        break