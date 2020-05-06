from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    q = deque()
    result = ''
    for _ in range(N):
        command = list(input().split())
        if command[0] == '1':
            q.append(command[1])
        else:
            if len(q) == 0:
                result += '-1 '
            else:
                a = max(q)
                result += a + ' '
                q.remove(a)
    print('#{} {}'.format(tc, result))
