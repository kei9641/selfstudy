result = []
T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    result.append(A+B)
for i in range(T):
    print('#{} {}'.format(i+1, result[i]))