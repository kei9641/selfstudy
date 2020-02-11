# S = input()
# tag = []
# reverseTag = []
# slicing = 0
# for i in range(len(S)):
#     if S[i] =='<':
#         if S[slicing] == '>':
#             if len(S[slicing+1:i]) != 0:
#                 tag.append(S[slicing+1:i])
#         else:
#             if len(S[slicing:i]) != 0:
#                 tag.append(S[slicing:i])

#         for n in range(1, len(S)-i):
#             if S[i+n] == '>':
#                 tag.append(S[i:i+n+1])
#                 slicing = i+n
#                 break
# if slicing != 0:
#     if len(S[slicing+1:i+1]) != 0:
#         tag.append(S[slicing+1:i+1])
# if '<' not in S:
#     tag.append(S)
# for i in range(len(tag)):
#     if '<' not in tag[i]:
#         tag[i] = ''.join(list(reversed(tag[i])))

# print(tag)


'''
1. 문장으로 끝나는 경우
2. <> 0개 + 문장
'''
S = list(input())
start = 0
end = 0
for i in range(len(S)):
    if S[i] =='<':
        for n in range(1, len(S)-i):
            if S[i+n] == '>':
                start = i+n+1
                break

    for m in range(len(S)-start):
        if S[start+m].isalpha() == True:
            for l in range(1, len(S)-start-m):
                if S[start+m+l].isalpha() == False:
                    end = start+m+l-1
                    for j in range((start+m + end) // 2):
                        S[start+m+j] = S[end-j]

        elif S[start+m] == '<':
            break
        
        

    else:
        jump += 1