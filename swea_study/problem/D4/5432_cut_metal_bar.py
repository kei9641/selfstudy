T = int(input())
for tc in range(1, T+1):
    position = list(input())
    result = 0
    count = 0
    for i in range(len(position)):
        if position[i] == '(':
            count += 1
        elif position[i] == ')':
            if position[i-1] == '(':
                count -= 1
                result += count
            else:
                count -= 1
                result += 1                          
    print('#{} {}'.format(tc, result))
