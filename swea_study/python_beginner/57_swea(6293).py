# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 17

'''
다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아
이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.

예제 입력)
2, 3, 4, 5 

예제 출력)
12.57, 18.85, 25.13, 31.42 
'''

# solution 1

Pi = 3.141592
input_str = input().split(', ')
circle = 0

for i in range(len(input_str)-1):
    input_num = int(input_str[i])
    circle = 2 * Pi * input_num
    print('{:.2f}'.format(circle), end=', ')
input_num = int(input_str[-1])
circle = 2 * Pi * input_num
print('{:.2f}'.format(circle))
