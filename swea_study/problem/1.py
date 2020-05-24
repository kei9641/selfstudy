T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = []
    for _ in range(M):
        data.append(list(map(int, input().split())))
    group = [0 for _ in range(N+1)]
    connect = []
    n = 1
    for i in range(M):
        if len(data[i]) == 2:
            p1, p2 = data[i]
            if group[p1] == 0 and group[p2] == 0:
                group[p1] = n
                group[p2] = n
                n += 1
            elif group[p1] == 0:
                group[p1] = group[p2]
            elif group[p2] == 0:
                group[p2] = group[p1]
            elif group[p1] != group[p2]:
                if group[p1] < group[p2]:
                    link = [group[p1], group[p2]]
                else:
                    link = [group[p2], group[p1]]
                if link not in connect:
                    connect.append(link)
    m = 0
    if len(connect) > 2:
        for i in range(2, len(connect)):
            n1, n2 = connect[i]
            n0 = 0
            for j in range(i):
                if n1 == connect[j][0]:
                    n0 = connect[j][1]
                if n0 == connect[j][0]:
                    m += 1

    result = max(group) - len(connect) + group.count(0) - 1 + m
    print('#{} {}'.format(tc, result))
