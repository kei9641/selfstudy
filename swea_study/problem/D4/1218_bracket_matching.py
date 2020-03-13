T = 10
for tc in range(1, T+1):
    N = int(input())
    bracket = list(input())
    openBracket = ['(', '[', '{', '<']
    closeBracket = [')', ']', '}', '>']
    result = 1
    check = []
    for i in range(N):
        if bracket[i] in closeBracket:
            if check == []:
                result = 0
                break
            elif closeBracket.index(bracket[i]) != openBracket.index(check[-1]):
                result = 0
                break
            else:
                check.pop()
        elif bracket[i] in openBracket:
            check.append(bracket[i])
    print('#{} {}'.format(tc, result))
    
