T = int(input())
for tc in range(T):
    text = list(input())
    H = int(input())
    position = list(map(int, input().split()))
    sound = ''
    for i in range(len(text)):
        sound += '-' * position.count(i)
        sound += text[i]
    sound += '-' * position.count(len(text))
    print('#{} {}'.format(tc+1, sound))
