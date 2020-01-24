# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 2

'''
다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
(단, 약수가 2개일 경우 소수임을 나타내십시오)

예제 입력)
5

예제 출력)
1(은)는 5의 약수입니다.
5(은)는 5의 약수입니다.
5(은)는 1과 5로만 나눌 수 있는 소수입니다.
'''

positive_number = int(input())
count = 0
for i in range(1, positive_number+1):
    if(positive_number%i==0):
        print("%d(은)는 %d의 약수입니다." %(i, positive_number))
        count = count + 1
if(count == 2):
    print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." %(positive_number, positive_number))