T = int(input())
for tc in range(T):
    s = input()
    for n in range(1, 10):
        if len(s) > 2*n:
            if s[:n] == s[n:2*n]:
                print('#{} {}'.format(tc+1, n))
                break
            
