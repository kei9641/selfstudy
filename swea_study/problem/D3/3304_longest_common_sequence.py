T = int(input())
for tc in range(1, T+1):
    A, B = map(list, input().split())
    check = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
    for i in range(1, len(B)+1):
        for j in range(1, len(A)+1):
            if A[j-1] == B[i-1]:
                check[i][j] = check[i-1][j-1]+1
            else:
                check[i][j] = max(check[i-1][j], check[i][j-1])
    print('#{} {}'.format(tc, check[-1][-1]))