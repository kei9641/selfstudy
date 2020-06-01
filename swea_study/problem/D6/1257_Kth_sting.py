T = int(input())
for tc in range(1, T+1):
    K = int(input())
    S = input()
    words = []
    N = len(S)
    for i in range(N):
        for j in range(i+1, N+1):
            words.append(S[i:j])
    words = sorted(list(set(words)))
    if K > len(words):
        print('#{} none'.format(tc))
    else:
        print('#{} {}'.format(tc, words[K-1]))