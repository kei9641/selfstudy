T = 10
for _ in range(T):
    tc = int(input())
    word = input()
    string = input()
    print('#{} {}'.format(tc, string.count(word)))