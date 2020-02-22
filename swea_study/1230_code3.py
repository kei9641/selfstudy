import sys
sys.stdin = open('code3.txt')

T = 10
for tc in range(T):
    Ns = int(input())
    original = list(input().split())
    Nc = int(input())
    commends = list(input().split())
    for idx in range(len(commends)):
        if commends[idx] == 'I':
            for n in range(int(commends[idx+2])):
                original.insert(int(commends[idx+1])+n, int(commends[idx+2+n+1]))
        elif commends[idx] == 'D':
            for _ in range(int(commends[idx+2])):
                del original[int(commends[idx+1])]
        elif commends[idx] == 'A':
            for n in range(1, int(commends[idx+1])+1):
                original.append(int(commends[idx+1+n]))
    print('#{}'.format(tc+1),end=' ')
    for i in range(10):
        print(original[i], end=' ')
    print()
