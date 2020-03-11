T = int(input())
for tc in range(1, T+1):
    numbers = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }
    N, M = map(int, input().split())
    binary = []
    for _ in range(N):
        binary.append(input())
    linX, lineY = 0, 0
    for x in range(N-1, -1, -1):
        if binary[x] != '0'*M:
            for y in range(M-1, -1, -1):
                if binary[x][y] == '1':
                    lineX, lineY = x, y
                    break
            if lineX != 0:
                break
    code = binary[lineX][lineY-55:lineY+1]
    decode = []
    for s in range(0, 56, 7):
        decode.append(numbers[code[s:s+7]])
    even, odd = 0, 0
    for i in range(7):
        if i % 2:
            even += decode[i]
        else:
            odd += decode[i]
    if (odd*3+even+decode[-1])%10 == 0:
        result = sum(decode)
    else:
        result = 0
    print('#{} {}'.format(tc, result))