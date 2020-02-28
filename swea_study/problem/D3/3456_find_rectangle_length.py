T = int(input())
for tc in range(T):
    side = list(map(int, input().split()))
    if side[0] == side[1]:
        print('#{} {}'.format(tc+1, side[2]))
    else:
        if side[0] == side[2]:
            print('#{} {}'.format(tc+1, side[1]))
        else:
            print('#{} {}'.format(tc+1, side[0]))
