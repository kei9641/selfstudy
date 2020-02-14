T = int(input())
for tc in range(T):
    words = []
    sentence = ''
    for _ in range(5):
        words.append('{:''<15}'.format(input()))
    for j in range(15):    
        for i in range(len(words)):
            sentence += words[i][j]
    print('#{}'.format(tc+1), end=' ')
    print(sentence.replace(' ', ''))