import sys
sys.stdin = open('pool.txt')

def charge(n):
    global result, fee
    if visited == [1]*12:
        if result > fee:
            result = fee
        fee = 0
        return
    for i in range(n, 12):
        m = 0
        d = 0
        if visited[i] == 0 and visited[i-1] == 0 and visited[i-2] == 0:
            visited[i] = 1
            visited[i-1] = 1
            visited[i-2] = 1
            if plan[i] > maxDay:
                if i == 0 or i == 1:
                    fee += M
                else:
                    m += 1
            else:
                if i == 0 or i == 1:
                    fee += plan[i] * D
                else:
                    d += plan[i]
            if plan[i-1] > maxDay:
                if i == 1:
                    fee += M
                else:
                    m += 1
            else:
                if i == 1:
                    fee += plan[i-1] * D
                else:
                    d += plan[i-1]
            if plan[i-2] > maxDay:
                m += 1
            else:
                d += plan[i-2]
            
            if m*M+d*D > Th:
                fee += Th
            else:
                fee += m*M+d*D
                # if i == 0:
                #     if plan[i] > maxDay:
                #         fee += M
                #     else:
                #         fee += plan[i] * D
                # elif i == 1:
                #     if plan[i] > maxDay:
                #         fee += M
                #     else:
                #         fee += plan[i] * D
                #     if plan[i-1] > maxDay:
                #         fee += M
                #     else:
                #         fee += plan[i-1] * D
            charge(i+3)
            visited[i] = 0
            visited[i-1] = 0
            visited[i-2] = 0

T = int(input())
for tc in range(T):
    D, M, Th, Y = map(int, input().split())
    plan = list(map(int, input().split()))
    maxDay = M//D
    visited = [0 for _ in range(12)]
    result = Y
    fee = 0
    charge(0)
    print('#{} {}'.format(tc+1, result))
