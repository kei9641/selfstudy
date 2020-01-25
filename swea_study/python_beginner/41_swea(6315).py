# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 8

'''
1~10까지의 정수를 항목으로 갖는 리스트 객체에서 map 함수와 람다식을 이용해
항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.

예제 출력)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
'''

'''
# 1. map(함수, 리스트) : 리스트 값을 차례대로 하나씩 함수에 대입
a = [1, 2, 3, 4, 5, 6]
def make_double(x):
	return x * 2

result = list(map(make_double, a))
print(result)

# 2. lambda 입력값: 명령문 : 입력값을 명령문에 대입하여 나온 값을 반환
a = lambda x: x+5
b = a(7)
print(b)
'''
a = range(1, 11)
b = list(map(lambda x : x ** 2, a))
print(b)
