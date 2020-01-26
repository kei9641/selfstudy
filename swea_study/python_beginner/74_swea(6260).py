# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 3. 자료구조 - 셋, 딕셔너리 8

'''
다음과 같이 사용자가 입력한 문장에서 대소문를 구별해 각각의 갯수를 출력하는 프로그램을 작성하십시오.

예제 입력)
Hello World! 123 

예제 출력)
UPPER CASE 2
LOWER CASE 8
'''

sentence = input()
upper_cnt = 0
lower_cnt = 0

for word in sentence:
    if word.isupper():
        upper_cnt += 1
    elif word.islower():
        lower_cnt += 1
print('UPPER CASE {}' . format(upper_cnt))
print('LOWER CASE {}' .format(lower_cnt))
