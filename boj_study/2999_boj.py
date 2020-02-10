message = input()

# 행, 열 크기 찾기
N = len(message)
R = int(N**(1/2))
C = int(N / R)
while R * C != N:
    R -= 1
    C = int(N / R)

texts = [[0] * C for _ in range(R)]
idx = 0

# R x C 행렬에 입력문자 넣기
for y in range(C):
    for x in range(R):
        texts[x][y] = message[idx]
        idx += 1
# 암호 해독해서 출력
for x in range(R):
    for y in range(C):
        print(texts[x][y], end='')
