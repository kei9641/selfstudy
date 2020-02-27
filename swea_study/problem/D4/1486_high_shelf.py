T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    clerk = list(map(int, input().split()))
    n = len(clerk)
    height = []
    for i in range(1 << n):
        h = 0
        for j in range(n):
            if i & (1 << j):
                h += clerk[j]
        height.append(h)
    result = list(set(height))
    result.sort()
    for i in range(len(result)):
        if result[i] >= B:
            print('#{} {}'.format(tc+1, result[i]-B))
            break
    