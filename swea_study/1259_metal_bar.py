T = int(input())
for tc in range(T):
    N = int(input())
    nasa = list(map(int, input().split()))
    bolt = nasa[::2]
    nut = nasa[1::2]
    firstIdx = 0

    for i in range(len(bolt)): # 막대 첫 나사 찾기
        first = True
        for j in range(len(nut)):
            if bolt[i] == nut[j]:
                first = False
        if first == True:
            firstIdx = i * 2
            break

    for k in range(0, len(nasa) - 1, 2): # 연결 나사 찾기
        nasa[k], nasa[k + 1], nasa[firstIdx], nasa[firstIdx + 1] = nasa[firstIdx], nasa[firstIdx + 1], nasa[k], nasa[k + 1]
        bolt = nasa[::2]
        for i in range(len(bolt)):
            if nasa[k + 1] == bolt[i]:
                firstIdx = i * 2
    print('#{}'.format(tc+1), end=' ')
    for idx in range(len(nasa)-1):
        print(nasa[idx], end=' ')
    print(nasa[-1])