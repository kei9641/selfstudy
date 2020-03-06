result =[]

T = int(input())
for tc in range(T):
    N = int(input())
    points = list(map(int, input().split()))
    scores = [0] * (sum(points)+1)
    scores[0] = 1
    for n in range(N-1, -1, -1):
        for i in range(len(scores)-1, -1, -1):
            if scores[i] == 1:
                scores[i+points[n]] = 1
    result.append(scores.count(1))

for i in range(T):
    print('#{} {}'.format(i+1, result[i]))

# 조합은 시간이 너무 많이 걸림..
# for문으로 2^N 해도 안됨..