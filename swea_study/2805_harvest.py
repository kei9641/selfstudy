T = int(input())
for tc in range(T):
    N = int(input())
    area = [[0]*N for _ in range(N)]
    harvest = 0
    for i in range(N):
        product = input()
        for j in range(N):
            area[i][j] = int(product[j])
    if N == 1:
        harvest = sum(area[0])
    else:
        for x in range(N):
            if x < N//2:
                for y in range(N//2-x, N//2+x+1):
                    harvest += area[x][y]
            else:
                for y in range(x-N//2, N-x+N//2):
                    harvest += area[x][y]
    print('#{} {}'.format(tc+1, harvest))