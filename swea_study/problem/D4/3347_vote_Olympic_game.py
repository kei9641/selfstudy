T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    vote = [0]*N
    for i in range(M):
        for j in range(N):
            if B[i] >= A[j]:
                vote[j] += 1
                break
    score = 0
    game = 1
    for i in range(N):
        if vote[i] > score:
            score = vote[i]
            game = i+1
    print('#{} {}'.format(tc, game))