T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    array = []
    for _ in range(M):
        array.append(list(map(int, input().split())))
    result = array[0]
    for i in range(1, M):
        for j in range(len(result)):
            if array[i][0] < result[j]:
                result[j:0] = array[i]
                break
        else:
            result += array[i]
    print('#{}'.format(tc), end=' ')
    idx = 1
    while idx < 10:
        print(result[len(result)-idx], end=' ')
        idx += 1
    print(result[-10])

# 리스트 전체를 insert하기
# result[x:0] = [1, 2, 3]
