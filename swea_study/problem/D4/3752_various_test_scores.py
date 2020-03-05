result =[]

def cal(n, k, s):
    global total
    if n == k:
        if total not in scores:
            scores.append(total)
        return
    if s == 1:
        total += points[n]
    cal(n+1, k, 0)
    cal(n+1, k, 1)
    if s == 1:
        total -= points[n]

T = int(input())
for tc in range(T):
    N = int(input())
    points = list(map(int, input().split()))
    scores = []
    total = 0
    cal(0, N, 0)
    cal(0, N, 1)
    result.append(len(scores))

for i in range(T):
    print('#{} {}'.format(i+1, result[i]))