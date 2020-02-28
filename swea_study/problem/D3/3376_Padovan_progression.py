result = []
T = int(input())
for tc in range(T):
    N = int(input())
    progression = [0, 1, 1, 1, 2]
    for i in range(5, N+1):
        progression.append(progression[i-1]+progression[i-5])
    result.append(progression[N])

for i in range(T):
    print('#{} {}'.format(i+1, result[i]))

# 재귀쓰면 시간초과