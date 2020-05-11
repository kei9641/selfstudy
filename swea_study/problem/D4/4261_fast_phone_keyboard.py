keyboard = {
    'a': 2,
    'b': 2,
    'c': 2, 
    'd': 3,
    'e': 3,
    'f': 3, 
    'g': 4,
    'h': 4, 
    'i': 4, 
    'j': 5, 
    'k': 5,
    'l': 5, 
    'm': 6,
    'n': 6,
    'o': 6, 
    'p': 7,
    'q': 7,
    'r': 7,
    's': 7, 
    't': 8,
    'u': 8,
    'v': 8, 
    'w': 9,
    'x': 9,
    'y': 9,
    'z': 9
}

T = int(input())
for tc in range(1, T+1):
    S, N = input().split()
    N = int(N)
    S = list(map(int, S))
    L = len(S)
    count = 0
    words = list(input().split())
    for i in range(N):
        if L == len(words[i]):
            for j in range(L):
                if keyboard[words[i][j]] != S[j]:
                    break
            else:
                count += 1
    print('#{} {}'.format(tc, count))