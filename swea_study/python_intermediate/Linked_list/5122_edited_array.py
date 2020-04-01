T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    command = []
    for _ in range(M):
        command.append(list(input().split()))
    for i in range(M):
        if command[i][0] == 'I':
            arr.insert(int(command[i][1]), int(command[i][2]))
        elif command[i][0] == 'D':
            arr.pop(int(command[i][1]))
        elif command[i][0] == 'C':
            arr[int(command[i][1])] = int(command[i][2])
    result = -1
    if 0 <= L < len(arr):
        result = arr[L]
    print('#{} {}'.format(tc, result))