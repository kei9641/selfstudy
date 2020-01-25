# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 4

'''
"ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와
같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된
알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오. 

예제 출력)
184
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

a = list('ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC')
b = list(map(lambda x : ord('E') - ord(x), a))
print(sum(b))
