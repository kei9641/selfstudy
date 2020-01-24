# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 4

'''
1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.

예제 출력)
1, 3, 5, 7, 9, ... 95, 97, 99 
'''

# solution 1

s1 = list()
for i in range(1, 101):
    if((i%2) != 0):
        s1.append(i)
for i in range(len(s1)-1):
    print("%d" %(s1[i]), end = ", ")
print(s1[-1])

# solution 2

odd_number = list()

for i in range(1, 101):
    if i % 2:
        odd_number.append(i)

for i in range(len(odd_number)-1):
    print(odd_number[i], end=', ')
print(odd_number[-1])