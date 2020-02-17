T = int(input())
for tc in range(T):
    N = int(input())
    string = input()
    endString = ['.', '?', '!']
    prei = 0
    nameCnt = []
    talks = []
    for idx in range(len(string)): # 구두점으로 문장 나눔 talks
        if string[idx] in endString:
            talks.append(string[prei:idx])
            prei = idx+1
    for i in range(N): 
        count = 0
        words = talks[i].split() # 공백으로 문장을 단어로 나눔 words
        isname = False
        for word in words:
            if word.isalpha() == True and word[0].isupper() == True: # 알파벳으로 이루어지고 첫글자가 대문자이면 True
            #     isname = True
            #     for j in range(1, len(word)): # 만약 첫글자를 제외한 글자가 대문자이면 False
            #         if word[j].isupper() == True:
            #             isname = False
            # if isname == True:
                count += 1
        nameCnt.append(count)
    print('#{}'.format(tc+1), end=' ')
    print(*nameCnt)
