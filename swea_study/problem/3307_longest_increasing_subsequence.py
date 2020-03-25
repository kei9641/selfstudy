T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    # 증가 수열을 만들 수 있는 경우의 수
    cnt = [0] * N
    # i보다 큰 index에서 A[i]보다 크거나 같은 수를 count
    for i in range(N):
        c = 0
        for j in range(i+1, N):
            if A[i] <= A[j]:
                c += 1
        cnt[i] = c
    # 중복되는 경우를 제거한 뒤 최장 부분 증가 수열의 길이
    result = len(set(cnt))
    print('#{} {}'.format(tc, result))
