n = int(input())
for i in range(1, n+1):
    if i != n:
        print(' ' * (2*(n-i)-1), end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    print()