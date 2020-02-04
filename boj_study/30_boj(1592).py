N, M, L = map(int, input().split())
receive = [0] * N
i = 0
count = 0
while 1:
    receive[i] += 1
    if receive[i] == M:
        break
    if receive[i] % 2: # 받은 횟수 홀수면 시계 방향 L
        if i + L >= N:
            i -= N
        i += L
    else: # 받은 횟수 짝수면 반시계 방향 L
        if i - L < 0:
            i += N
        i -= L
    count += 1

print(count)