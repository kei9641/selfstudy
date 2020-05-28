# testcase 바뀜
T = int(input())
for tc in range(1, T+1):
    card, N = map(int, input().split())
    turns = [[] for _ in range(N+1)]
    turns[0].append(card)
    digit = len(str(card))
    n = 0
    while n < N:
        for turn in turns[n]:
            price = list(str(turn))
            while len(price) < digit:
                price.insert(0, '0')
            for i in range(digit-1):
                for j in range(i+1, digit):
                    swap = price[:]
                    swap[j], swap[i] = swap[i], swap[j]
                    num = int(''.join(swap))
                    if num not in turns[n+1]:
                        turns[n+1].append(num)
        n += 1
    print('#{} {}'.format(tc, max(turns[-1])))

