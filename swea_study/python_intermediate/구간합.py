# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합
import sys
sys.stdin = open("구간합.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    start = 0
    finish = M
    min_num = 987654321
    max_num = 0
    
    while finish <= N:
        sum_part = 0
        for i in range(start, finish):
            sum_part += a[i]
        if sum_part < min_num:
            min_num = sum_part
        if sum_part > max_num:
            max_num = sum_part
        start += 1
        finish += 1

    result = max_num - min_num
    print('#{} {}'.format(tc+1, result))