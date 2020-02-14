T = int(input())
for tc in range(T):
    m1, d1, m2, d2 = map(int, input().split())
    max_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m1 == m2:
        date = d2 - d1 + 1
    else:
        date = d2
        for i in range(m1, m2):
            if m1 == i:
                date += max_day[i-1] - d1 + 1
            else:
                date += max_day[i-1]
    print('#{} {}'.format(tc+1, date))