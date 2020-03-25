# 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드
import sys
sys.stdin = open("숫자_카드.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    a = list(str(input()))
    count = [0] * 10
    for ai in a:
        count[int(ai)] += 1
    maxCount = count[0]
    maxIdx = 0
    for i in range(len(count)):
        if maxCount <= count[i]:
            maxCount = count[i]
            maxIdx = i
        
    print('#{} {} {}'.format(tc+1, maxIdx, maxCount))