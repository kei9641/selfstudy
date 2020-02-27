def palindrome(a):
    result = True
    for i in range(len(a)):
        if a[i] != a[-(i+1)]:
            result = False
    return result

T = 10
for tc in range(T):
    N = 8
    rowCnt = 0
    columnCnt = 0
    M = int(input())
    strings = []
    for _ in range(N): # 글자판 만들기
        strings.append(input())
    for x in range(N):
        start = 0
        end = M
        while end <= N:
            M_str = strings[x][start:end] # M 길이만큼 자르기
            start += 1
            end += 1
            if palindrome(M_str) == True: # 자른 문자가 회문이면
                rowCnt += 1

    lines = [] # 가로 <-> 세로
    for x in range(N):
        line = ''
        for y in range(N):
            line += strings[y][x]
        lines.append(line)

    for x in range(N):
        start = 0
        end = M
        while end <= N:
            M_str = lines[x][start:end]
            start += 1
            end += 1
            if palindrome(M_str) == True:
                columnCnt += 1

    print('#{} {}'.format(tc+1, rowCnt + columnCnt))