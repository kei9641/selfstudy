T = int(input())
for tc in range(T):
    cards = []
    count = [13, 13, 13, 13]
    string = input()
    for i in range(0, len(string), 3):
        cards.append(string[i] + string[i+1] + string[i+2])
    duple = True
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            if cards[i] == cards[j]:
                duple = False
                break
    for i in range(len(cards)):
        if cards[i][0] == 'S':
            count[0] -= 1
        elif cards[i][0] == 'D':
            count[1] -= 1
        elif cards[i][0] == 'H':
            count[2] -= 1
        elif cards[i][0] == 'C':
            count[3] -= 1
    print('#{}'.format(tc+1), end=' ')
    if duple == True:
        print(*count)
    else:
        print('ERROR')