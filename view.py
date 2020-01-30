import sys
sys.stdin = open("view_input.txt")

# max, min, count, sort 함수 x

T = 10

for tc in range(T):

    N = int(input())
    data = list(map(int, input().split()))
    height = []
    next_max = 0
    result = 0
    sight = 0

    for i in range(2, len(data)-2):
        left = data[i-2:i]
        right = data[i+1:i+3]
        neighbor = left + right # 양 옆으로 두 값을 저장한 리스트
        next_max = 0

        for floor in neighbor:

            if data[i] < floor:

                continue

            else:
                if next_max < floor:
                    next_max = floor
        result = data[i] - next_max


        height.append(result)
    # for h in height:
    #     sight += h



    print(height)




    # print("#{} {}".format(tc+1, ans))


'''
(각 값) - (양 옆으로 두 값들 중 가장 큰 값) = 결과값
만약 각 값 <= 양 옆으로 두 값 이면 패스
모든 인덱스의 결과값을 합하기
'''