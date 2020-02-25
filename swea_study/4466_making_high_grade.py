T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    grade = 0
    for _ in range(K):
        grade += max(scores)
        scores.remove(max(scores))
    print('#{} {}'.format(tc+1, grade))