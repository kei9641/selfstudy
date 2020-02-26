T = int(input())
for tc in range(T):
    texts = list(input())
    read = []
    vowels = 'aeiou'
    for text in texts:
        if text not in vowels:
            read.append(text)
    print('#{}'.format(tc+1),end=' ')
    print(''.join(read))