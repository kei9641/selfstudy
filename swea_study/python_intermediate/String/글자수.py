import sys
sys.stdin = open('글자수.txt')

T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    words = list(set(str1))
    dicWord = {}
    maxWord = 0
    for word in words:
        if word in str2:
            if word in dicWord:
                dicWord[word] += str2.count(word)
            else:
                dicWord[word] = str2.count(word)
    for val in dicWord.values():
        if maxWord < val:
            maxWord = val
    print('#{} {}'.format(tc+1, maxWord))

