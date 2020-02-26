T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    student = []
    for num in range(1, N+1):
        student.append(num)
    submit = list(map(int, input().split()))
    for i in submit:
        student.remove(i)
    student.sort()
    print('#{}'.format(tc+1),end=' ')
    print(*student)