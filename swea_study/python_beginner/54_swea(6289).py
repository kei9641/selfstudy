# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 13

'''
사용자가 숫자를 입력하면 숫자의 각 자릿수의 합을 구해서 반환하는 프로그램을 작성하십시오.
예를 들어 123을 입력하면 1 + 2 + 3 = 6의 결과를 반환합니다.

예제 입력)
12345

예제 출력)
15
'''

numbers = input()
result = 0

for i in range(len(numbers)):
    result += int(numbers[i])
print(result)