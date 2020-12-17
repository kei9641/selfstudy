# 입력
N = int(input())

# 최소 생성자 구하기
strN = str(N)
minN = N - (int(strN[0]) + 9 * (len(strN)-1))

# 생성자 찾기
for i in range(minN, N+1):
    divideN = list(map(int, str(i)))
    generateN = sum(divideN) + i
    if generateN == N:
        print(i)
        break
else:
    print(0)