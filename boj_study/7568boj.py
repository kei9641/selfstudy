#  선언
body = []

# 입력
N = int(input())
for _ in range(N):
    weight, height = map(int, input().split())
    body.append((weight, height))

# 덩치 비교
rank = [1] * N
for i in range(N):
    for j in range(i+1, N):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            rank[i] += 1
        elif body[i][0] > body[j][0] and body[i][1] > body[j][1]:
            rank[j] += 1

# 출력
print(*rank)