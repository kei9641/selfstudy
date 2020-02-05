n = int(input())
turnAlpha = 0
turnNum = 0
for i in range(n):
    for j in range(i, n):
        print(chr(ord('A') + turnAlpha), end=' ')
        turnAlpha += 1        
    for j in range(i):
        print((turnNum), end=' ')
        turnNum += 1
    print()
