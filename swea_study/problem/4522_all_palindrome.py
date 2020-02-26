T = int(input())
for tc in range(T):
    pattern = list(input())
    result = True
    change = '?'
    for i in range(len(pattern)):
        if pattern[i] != pattern[-(i+1)]:
            if pattern[i] == '?' and pattern[-(i+1)] != '?':
                change = pattern[-(i+1)]
            elif pattern[i] != '?' and pattern[-(i+1)] == '?':
                change = pattern[i]
        if pattern[i] == '?':
            pattern[i] = change

    for i in range(len(pattern)):
        if pattern[i] != pattern[-(i+1)]:
            result = False
    
    if result == True:
        print('#{} Exist'.format(tc+1))
    else:
        print('#{} Not exist'.format(tc+1))