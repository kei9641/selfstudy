# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 3. 자료구조 - 셋, 딕셔너리 10

'''
다음의 결과와 같이 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하십시오.

예제 입력)
abcdefgabc 

예제 출력)
a,2
b,2
c,2
d,1
e,1
f,1
g,1
'''

word_cnt = {}
words = input()

for word in words:
    word_cnt[word] = words.count(word)

for word, cnt in word_cnt.items():
    print('{},{}' .format(word, cnt))