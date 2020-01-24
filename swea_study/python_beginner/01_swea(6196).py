# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 4. 변수

'''
1~9 사이의 정수 a를 입력받아 a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.

예제 입력)
9

예제 출력)
11106
'''
# solution 1

a = int(input())
b=int(str(a)) + int(str(a)+str(a)) + int(str(a)+str(a)+str(a)) + int(str(a)+str(a)+str(a)+str(a))
print(b)


# solution 2

input_number = input()
string_a = ''
number_a = 0
if len(input_number) == 1:
    for i in range(1, 5):
        string_a = input_number * i
        number_a += int(string_a)
print(number_a)

