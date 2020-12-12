N, r, c = map(int, input().split())

r += 1
c += 1
startR, endR, startC, endC = 1, 2**N, 1, 2**N
startS, endS = 1, endR * endC

line = 0
while startS != endS:
    if line % 2:
        midC = (startC + endC) // 2
        if midC < c:
            startC = midC + 1
            startS = (startS + endS) // 2 + 1
        else:
            endC = midC
            endS = (startS + endS) // 2
    else:
        midR = (startR + endR) // 2
        if midR < r:
            startR = midR + 1
            startS = (startS + endS) // 2 + 1
        else:
            endR = midR
            endS = (startS + endS) // 2
    line += 1

print(startS-1)
