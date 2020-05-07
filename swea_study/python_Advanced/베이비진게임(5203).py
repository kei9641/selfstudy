import syssys.stdin = open('베이비진게임(5203).txt')

def babygin(a, b):
    checkA = [0] * 10
    checkB = [0] * 10
    for i in range(idx//2+1):
        checkA[a[i]] += 1
        checkB[b[i]] += 1
    for j in range(10):
        if checkA[j] >= 3:
            return 1
    for j in range(8):
        if checkA[j] >= 1 and checkA[j+1] >= 1 and checkA[j+2] >= 1:
            return 1
    for k in range(10):
        if checkB[k] >= 3:
            return 2
    for k in range(8):
        if checkB[k] >= 1 and checkB[k+1] >= 1 and checkB[k+2] >= 1:
            return 2
    return 0

result = []
T = int(input())
for tc in range(T):
    shuffle = list(map(int, input().split()))
    player1 = []
    player2 = []
    winner = 0
    for idx in range(0, 12, 2):
        player1.append(shuffle[idx])
        player2.append(shuffle[idx+1])
        if idx >= 6:
            winner = babygin(player1, player2)
        if winner:
            break
    result.append(winner)

for i in range(T):
    print('#{} {}'.format(i+1, result[i]))