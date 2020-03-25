import sys
sys.stdin = open('종이붙이기.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    memo = [1, 3]
    for num in range(30, N+1, 10):
        if (num//10) % 2 == 0:
            memo.append(memo[(num//10)-2]*2+1)
        else:
            memo.append(memo[(num//10)-3]*4+1)
    print('#{} {}'.format(tc+1, memo[(num//10)-1]))