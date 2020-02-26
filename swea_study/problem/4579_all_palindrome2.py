T = int(input())
for tc in range(T):
    pattern = input()
    result = True
    for i in range(len(pattern)):
        if pattern[i] != pattern[-(i+1)]:
            result = False
            if pattern[i] == '*' or pattern[-(i+1)] == '*':
                result = True
    
    if result == True:
        print('#{} Exist'.format(tc+1))
    else:
        print('#{} Not exist'.format(tc+1))
