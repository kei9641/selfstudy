n = int(input())
odd = '13579'
repeat = 0
for _ in range(n):
    for _ in range(n):
        print(odd[repeat], end=' ')
        repeat += 1
        if repeat == 5:
            repeat = 0
    print()