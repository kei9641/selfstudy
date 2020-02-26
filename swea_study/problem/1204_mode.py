T = int(input())
for _ in range(T):
    tc = int(input())
    scores = list(map(int, input().split()))
    count = [0] * 101
    for score in scores:
        count[score] += 1
    for idx in range(100, -1, -1):
        if count[idx] == max(count):
            mode = idx
            break
    print('#{} {}'.format(tc, mode))
