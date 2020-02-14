T = int(input())
for tc in range(T):
    h1, m1, h2, m2 = map(int, input().split())
    if h1 + h2 > 12:
        hour = h1 + h2 - 12
    else:
        hour = h1 + h2
    if m1 + m2 >= 60:
        minute = m1 + m2 - 60
    else:
        minute = m1 + m2
    print('#{} {} {}'.format(tc+1, hour, minute))
