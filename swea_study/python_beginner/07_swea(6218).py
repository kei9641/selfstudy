# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 1

'''
다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오

예제 입력)
9

예제 출력)
1(은)는 9의 약수입니다.
3(은)는 9의 약수입니다.
9(은)는 9의 약수입니다.
'''

positive_number = int(input())
for i in range(1, positive_number+1) :
    divide_number = positive_number % i
    if(divide_number is 0):
        print("%d(은)는 %d의 약수입니다." %(i, positive_number))