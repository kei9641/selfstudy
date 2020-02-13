T = int(input())
for tc in range(T):
    ymd = input()
    day = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if 1 <= int(ymd[4:6]) <= 12 and 1 <= int(ymd[6:]) <= day[int(ymd[4:6])]:
        print('#{} {}/{}/{}'.format(tc+1, ymd[:4], ymd[4:6], ymd[6:]))
    else:
        print('#{} -1'.format(tc+1))