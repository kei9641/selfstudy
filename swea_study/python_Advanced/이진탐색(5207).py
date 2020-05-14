import sys
sys.stdin = open('이진탐색(5207).txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for num in B:
        l = 0
        r = N-1

        area = 0
        while 1:
            m = (l + r) // 2
            if num >= A[m]:
                if num == A[m]:
                    cnt += 1
                    break
                l = m + 1
                if area == 1: 
                    break
                area = 1
            elif num < A[m]:
                r = m - 1
                if area == 2: 
                    break
                area = 2

    print('#{} {}'.format(tc, cnt))