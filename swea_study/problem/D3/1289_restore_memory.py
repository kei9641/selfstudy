T = int(input())
for tc in range(1, T+1):
    memory = list(map(int, input()))
    change = 0
    bit = 0
    for i in range(len(memory)):
        if not memory[i] == bit:
            change += 1
            bit = not bit
    print('#{} {}'.format(tc, change))
