n = int(input())
turnNum = 1
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(i, n):
        print(turnNum, end=' ')
        turnNum += 1      
    print()
