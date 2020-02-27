T = int(input())
for tc in range(T):
    N = int(input())
    cards = list(input().split())
    deck = []
    if N % 2 == 0:
        middle = N//2
        for i in range(middle):
            deck.append(cards[i])
            deck.append(cards[middle+i])
    else:
        middle = N//2 + 1
        for i in range(middle-1):
            deck.append(cards[i])
            deck.append(cards[middle+i])
        deck.append(cards[middle-1])
    print('#{}'.format(tc+1),end=' ')
    print(*deck)
