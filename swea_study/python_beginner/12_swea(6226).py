# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 7

'''
1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아
콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.

예제 출력)
7,14,21,28,42,49,56,63,77,84,91,98,112,119,126,133,147,154,161,168,182,189,196 
'''

numbers = list()
for i in range(1, 200 + 1):
    if ((i%7)==0 and (i%5)!=0):
        numbers.append(i)

for i in range(len(numbers)-1) : 
    print("%d"%(numbers[i]), end=",")
print(numbers[-1])