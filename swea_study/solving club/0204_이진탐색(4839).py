import sys
sys.stdin = open('이진탐색.txt')

T = int(input())
for tc in range(T):
    Page, Pa, Pb = map(int, input().split())
    countA = 0
    countB = 0
    left = 1
    right = Page
    current = 0
    while Pa != current:
        current = int((left + right) / 2)
        if Pa < current:
            right = current
        elif Pa > current:
            left = current
        countA += 1
    left = 1
    right = Page
    while Pb != current:
        current = int((left + right) / 2)
        if Pb < current:
            right = current
        elif Pb > current:
            left = current
        countB += 1
    if countA > countB:
        result = 'B'
    elif countA < countB:
        result = 'A'
    elif countA == countB:
        result = 0
    print('#{} {}'.format(tc+1, result))
        
