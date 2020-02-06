import sys
sys.stdin = open("view_input.txt")

T = 10
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    sight = [0] * N # 각 인덱스 조망권 수

    for i in range(2, len(data)-2): # 거리 2이하인 이웃 높이 neighbor
        left, right = data[i-2:i], data[i+1:i+3]
        neighbors = left + right 
        maxNeighbor = neighbors[0]
        for j in range(1, len(neighbors)): # 가장 높은 이웃의 높이
            if maxNeighbor < neighbors[j]:
                maxNeighbor = neighbors[j]
        if data[i] > maxNeighbor: # 조망권 가구 수
            sight[i] = data[i] - maxNeighbor

    result = sum(sight) # 총 조망권 가구 수의 합
    print("#{} {}".format(tc+1, result))