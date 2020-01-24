# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 3

'''
다음의 결과와 같이 입력된 영어 알파벳 문자에 대해 대소문자를 구분하는 코드를 작성하십시오.

예제 입력)
b

예제 출력)
b 는 소문자 입니다. 
'''

alphabet = str(input())
if((alphabet >= 'a') & (alphabet <= 'z')):
    print("%s 는 소문자 입니다. " %alphabet)
elif((alphabet >= 'A') & (alphabet <= 'Z')):
    print("%s 는 대문자 입니다. " %alphabet)
else:
    print("")