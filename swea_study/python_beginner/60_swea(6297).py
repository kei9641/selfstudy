# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 20

'''
콤마(,)로 구분해 숫자를 입력하고, 입력된 숫자 중 홀수를 콤마(,)로 구분해 출력하는
리스트 내포 기능을 이용한 프로그램을 작성하십시오.

예제 입력)
1, 2, 3, 4, 5 

예제 출력)
1, 3, 5 
'''

numbers = list(map(int, input().split(', ')))
odds = [odd for odd in numbers if odd % 2]

for i in range(len(odds)-1):
    print(odds[i], end=', ')
print(odds[-1])