T = int(input())
for tc in range(1, T+1):
    K = int(input())
    S = input()
    suffixes = []
    for i in range(len(S)):
        suffixes.append(S[i:])
    suffixes.sort()
    if K > len(suffixes):
        print('#{} none'.format(tc))
    else:
        print('#{} {}'.format(tc, suffixes[K-1]))