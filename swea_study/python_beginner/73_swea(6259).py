# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 3. 자료구조 - 셋, 딕셔너리 7

'''
다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.

예제 입력)
hello world! 123 

예제 출력)
LETTERS 10
DIGITS 3
'''

sentence = input()
letter_cnt = 0
digit_cnt = 0

for word in sentence:
    if (('a' <= word <= 'z') or ('A' <= word <= 'Z')):
        letter_cnt += 1
    elif ('0' <= word <= '9'):
        digit_cnt += 1
print('LETTERS {}' .format(letter_cnt))
print('DIGITS {}' .format(digit_cnt))