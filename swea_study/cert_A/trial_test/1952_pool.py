import sys
sys.stdin = open('pool.txt')

T = int(input())
for tc in range(T):
    D, M, Th, Y = map(int, input().split())
    plan = list(map(int, input().split()))
    maxDay = M//D
    maxMonth = Th//D
    result = Y
    feeMD = 0
    # 3달권 X
    for i in range(12):
        if plan[i] > maxDay:
            feeMD += M
        else:
            feeMD += plan[i] * D
    # 3달권 O
    for i1 in range(12):
        feeTh = 0
        visited = [0] * 12
        if plan[i1] > 0:
            feeTh += Th
            visited[i1] = 1
            visited[i1-1] = 1
            visited[i1-2] = 1
            m = 0
            d = 0
            for j1 in range(12): 
                if visited[j1] == 0:
                    if plan[j1] > maxDay:
                        m += 1
                    else:
                        d += plan[i]
            if m*M + d*D > Th:
                for i2 in range(12):
                    if plan[i2] > 0 and visited[i2] == 0 and visited[i2-1] == 0 and visited[i2-2] == 0:
                        feeTh += Th
                        visited[i2] = 1
                        visited[i2-1] = 1
                        visited[i2-2] = 1
                        m = 0
                        d = 0
                        for j2 in range(12): 
                            if visited[j2] == 0:
                                if plan[j2] > maxDay:
                                    m += 1
                                else:
                                    d += plan[i]
                        if m*M + d*D > Th:
                            for i3 in range(12):
                                if plan[i3] > 0 and visited[i3] == 0 and visited[i3-1] == 0 and visited[i3-2] == 0:
                                    feeTh += Th
                                    visited[i3] = 1
                                    visited[i3-1] = 1
                                    visited[i3-2] = 1
                                    m = 0
                                    d = 0
                                    for j3 in range(12): 
                                        if visited[j3] == 0:
                                            if plan[j3] > maxDay:
                                                m += 1
                                            else:
                                                d += plan[i]
                                    if m*M + d*D > Th:
                                        feeTh = Th * 4
                                    else:
                                        feeTh += (m*M + d*D)
                        else:
                            feeTh += (m*M + d*D)
            else:
                feeTh += (m*M + d*D)
            # print(visited, i1)
            if feeTh != 0 and feeTh < feeMD:
                fee = feeTh
            else:
                fee = feeMD

    if result > fee:
        result = fee
    print('#{} {}'.format(tc+1, result))