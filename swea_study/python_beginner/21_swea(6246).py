# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 8

'''
while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.

예제 출력)
*****
****
***
**
*
'''

i = 5
while(i > 0):
    print("*" * i)
    i = i - 1