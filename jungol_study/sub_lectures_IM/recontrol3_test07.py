n = int(input())
turnAlpha = 0
turnNum = 1
for i in range(n):
    for j in range(i, n):
        print((turnNum), end=' ')
        turnNum += 1
    for j in range(i+1):
        print(chr(ord('A') + turnAlpha), end=' ')
        turnAlpha += 1
    print()