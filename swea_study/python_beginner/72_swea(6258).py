# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 3. 자료구조 - 셋, 딕셔너리 6

'''
다음과 같이 정수 N을 입력받아서 1부터 N까지의 정수를 키로 하고, 
그 정수의 제곱을 값으로 하는 딕셔너리 객체를 만드는 코드를 작성하십시오.

예제 입력)
5

예제 출력)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
'''

number = int(input())
squr = {}

for i in range(1, number+1):
    squr[i] = i ** 2
print(squr)