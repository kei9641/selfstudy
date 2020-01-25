# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 6

'''
ASCII 코드 값를 입력받아 문자를 확인하는 코드를 작성하십시오.

예제 입력)
65

예제 출력)
ASCII 65 => A 
'''

num = int(input())
string = chr(num)
print('ASCII {} => {}' .format(num, string))