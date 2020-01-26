# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 16

'''
콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.

예제 입력)
12, 34, 56, 78 

예제 출력)
[12, 34, 56, 78]
(12, 34, 56, 78)
'''

input_str = input().split(', ')
list_num = list()

for i in range(len(input_str)):
    list_num.append(int(input_str[i]))
tuple_num = tuple(list_num)
print(list_num)
print(tuple_num)