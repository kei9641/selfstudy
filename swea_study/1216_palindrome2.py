def palindrome(a):
    result = True
    for i in range(len(a)):
        if a[i] != a[-(i+1)]:
            result = False
    return result

T = 10
for tc in range(T):
    t = int(input())
    N = 100
    lengthMax = 1
    strings = []
    for _ in range(N): # 글자판 만들기
        strings.append(input())

    for x in range(N):
        for n in range(N-1):
            start = 0
            end = 1+n
            while end <= N:
                M_str = strings[x][start:end] # M 길이만큼 자르기
                start += 1
                end += 1
                if palindrome(M_str) == True: # 자른 문자가 회문이면
                    if lengthMax < len(M_str):
                        lengthMax = len(M_str)
                    break

    lines = [] # 가로 <-> 세로
    for x in range(N):
        line = ''
        for y in range(N):
            line += strings[y][x]
        lines.append(line)

    for x in range(N):
        for n in range(N-1):
            start = 0
            end = 1+n
            while end <= N:
                M_str = lines[x][start:end]
                start += 1
                end += 1
                if palindrome(M_str) == True:
                    if lengthMax < len(M_str):
                        lengthMax = len(M_str)
                    break

    print('#{} {}'.format(tc+1, lengthMax))