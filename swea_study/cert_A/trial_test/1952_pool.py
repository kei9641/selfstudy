import sys
sys.stdin = open('pool.txt')

def charge(n):
    global result, fee
    if n > 11:
        if result > fee:
            result = fee
        return

    for i in range(n, 12):
        m = 0
        d = 0
        if plan[i] > maxDay:
            m += 1
        else:
            d += plan[i]
        if i+1 <= 11:
            if plan[i+1] > maxDay:
                m += 1
            else:
                d += plan[i+1]
        if i+2 <= 11:
            if plan[i+2] > maxDay:
                m += 1
            else:
                d += plan[i+2]
        if m*M + d*D > Th:
            fee += Th
            fee -= m*M + d*D
            charge(i+3)
            fee -= Th
            fee += m*M + d*D
        else:
            charge(i+3)


T = int(input())
for tc in range(T):
    D, M, Th, Y = map(int, input().split())
    plan = list(map(int, input().split()))
    maxDay = M//D
    visited = [0 for _ in range(12)]
    result = Y
    fee = 0
    for i in range(12):
        if plan[i] > maxDay:
            fee += M
        else:
            fee += plan[i] * D
    charge(0)
    print('#{} {}'.format(tc+1, result))
