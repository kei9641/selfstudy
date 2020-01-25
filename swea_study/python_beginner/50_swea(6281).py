# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 7

'''
다음의 결과와 같이 정수를 입력하면 리스트 내포를 이용해
약수 리스트를 출력하는 코드를 작성하십시오.

예제 입력)
32

예제 출력)
[1, 2, 4, 8, 16, 32]
'''

number = int(input())
divide_num = [i for i in range(1, number+1) if (number % i == 0)]
print(divide_num)