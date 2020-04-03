T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stacks = []
    for _ in range(N):
        stacks.append(int(input()))
    hay = sum(stacks)//N
    move = 0
    for stack in stacks:
        if hay < stack:
            move += stack - hay
    print('#{} {}'.format(tc, move))