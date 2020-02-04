import sys
sys.stdin = open('metalBar.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    nasa = list(map(int, input().split()))
    bolt = nasa[::2]
    nut = nasa[1::2]
    firstIdx = 0
    # print(bolt)
    # print(nut)
    for i in range(len(bolt)):
        first = True
        for j in range(len(nut)):
            if bolt[i] == nut[j]:
                first = False
        if first == True:
            print(bolt[i])
            firstIdx = i * 2
            break

    for k in range(0, len(nasa)-1, 2):
        nasa[k], nasa[k+1], nasa[firstIdx], nasa[firstIdx+1] = nasa[firstIdx], nasa[firstIdx+1], nasa[k], nasa[k+1]
        chain = False
        for i in range(len(bolt)):
            if nasa[k+1] == bolt[i]:
                chain = True
        if chain == True:
            firstIdx = i * 2
            break
    print(nasa)


            

    # for num in bolt:
    #     cnt = 0
    #     for i in range(len(bolt)):
    #         if bolt[i] == num:
    #             cnt += 1
    #     count.append(cnt)
    # for i in range(len(count)):


