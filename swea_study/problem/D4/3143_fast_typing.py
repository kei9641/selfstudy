T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    print('#{} {}'.format(tc, len(A)-A.count(B)*(len(B)-1)))