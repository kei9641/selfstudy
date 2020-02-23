T = int(input())
for tc in range(T):
    m, d = map(int, input().split())
    month = [3, 6, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]
    week = d % 7 + month[m-1]
    if week > 6:
        week -= 7
    print('#{} {}'.format(tc+1, week))
