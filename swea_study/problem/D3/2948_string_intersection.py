T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(input().split())
    B = list(input().split())
    intersection = set(A + B)
    result = len(A) + len(B) - len(intersection)
    print('#{} {}'.format(tc, result))
# 수학공식의 중요성....