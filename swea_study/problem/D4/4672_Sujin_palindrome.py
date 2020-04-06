T = int(input())
for tc in range(1, T+1):
    words = input()
    alpha = dict()
    result = 0
    for word in words:
        if word in alpha:
            alpha[word] += 1
        else:
            alpha[word] = 1
    for n in alpha.values():
        result += (n*(n+1))//2
    print('#{} {}'.format(tc, result))