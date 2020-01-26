# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 18

'''
다음과 같이 2차원 배열 구조를 만들기 위한 행, 열 정보를 콤마(,)로 구분해 입력하고,
이 리스트 객체의 항목의 값은 행과 열의 인덱스 곱으로 초기화해 출력하는 프로그램을 작성하십시오.

예제 입력)
3, 5 

예제 출력)
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''

row = list()
column = list()

numbers = input()
number = list(map(int, numbers.split(', ')))

for i in range(number[0]):
    for j in range(number[1]):
        column.append(i*j)
    row.append(column)
    column = list()
print(row)
