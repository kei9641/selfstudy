message = input()
N = len(message)
R = int(N**(1/2))
C = int(N / R)
while R * C != N:
    R -= 1
    C = int(N / R)
texts = [[0] * C for _ in range(R)]
idx = 0
for x in range(R):
    for y in range(C):
        texts[x][y] = message[idx]
        idx += 1
for x in range(R):
    for y in range(C):
        print(texts[y][x], end='')

