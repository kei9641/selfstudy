# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 6

'''
다음의 결과와 같이 정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성하십시오.

예제 입력)
12

예제 출력)
[1, 2, 3, 4, 6, 12]
'''

number = int(input())
divide_num = list()

for i in range(1, number+1):
    if number % i == 0:
        divide_num.append(i)

print(divide_num)