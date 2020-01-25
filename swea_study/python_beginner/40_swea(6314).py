# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 7

'''
1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해
짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.

예제 출력)
[2, 4, 6, 8, 10] 
'''

'''
# 2. lambda 입력값: 명령문 : 입력값을 명령문에 대입하여 나온 값을 반환
a = lambda x: x+5
b = a(7)
print(b)
'''
a = range(1, 11)
def even(x):
    b = lambda x: (x % 2 == 0)
    return b(x)
result = list(filter(even, range(1, 11)))
print(result)