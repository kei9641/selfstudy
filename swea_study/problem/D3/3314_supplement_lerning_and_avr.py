T = int(input())
for tc in range(T):
    scores = list(map(int, input().split()))
    for i in range(5):
        if scores[i] < 40:
            scores[i] = 40
    print('#{} {}'.format(tc+1, sum(scores)//5))