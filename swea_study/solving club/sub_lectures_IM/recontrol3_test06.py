n = int(input())
turn = 0
for i in range(n):
    for j in range(i, n):
        print(chr(ord('A') + turn), end='')
        turn += 1
    print()
