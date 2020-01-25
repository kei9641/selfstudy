# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 6

'''
정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,
이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.

예제 출력)
[2, 4, 6, 8, 10]
5 => False
10 => True
'''

def selec(x, y): #x리스트 y특정숫자
    g = False
    for i in range(len(x)):
        if(x[i] == y):
            g = True
    return g

a = [2, 4, 6, 8, 10]
m, n = 5, 10
p = selec(a, m)
q = selec(a, n)
print(a)
print("{} => {}" .format(m, p))
print("{} => {}" .format(n, q))