n = int(input())
for _ in range(n):
    numeration = input()
    center = len(numeration)//2
    column = 0
    # transfer = ''
    if ord('1') <= ord(numeration[center]) <= ord('9'):
        for i in range(center):
            column += 26**(center-i-1)*(ord(numeration[i])-ord('A')+1)
        row = numeration[center:]
        transfer = 'R' + row + 'C' + column
    else:
        row = numeration[1:center]
        column = int(numeration[center+1:])
        while column // 26:
            +26
            column //= 26
