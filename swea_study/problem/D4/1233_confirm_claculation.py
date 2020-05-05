import sys
sys.stdin = open('1.txt')

T = 10
for tc in range(1, T+1):
    operation = '+-/*'
    N = int(input())
    leap = (N-1)//2
    result = 1
    if N % 2 == 0:
        result = 0
    for _ in range(1, N+1):
        node = list(input().split())
        if int(node[0]) <= leap:
            if node[1] not in operation:
                result = 0
        else:
            if node[1] in operation:
                result = 0
    print('#{} {}'.format(tc, result))