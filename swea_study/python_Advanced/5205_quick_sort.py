# import sys
# sys.stdin = open('.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    print('#{} {}'.format(tc, sorted(a)[N//2]))
    