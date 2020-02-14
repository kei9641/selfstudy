T = int(input())
for tc in range(T):
    s = input()
    for i in range(len(s)//2):
        if s[i] == s[-(i+1)]:
            print('#{} 1'.format(tc+1))
            break
        else:
            print('#{} 0'.format(tc+1))
            break