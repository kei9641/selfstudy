# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 5. 연산자 2

'''
킬로그램(kg)를 파운드(lb)으로 변환하는 프로그램을 작성하십시오.
이 때 1 킬로그램은 2.2046 파운드입니다.
   
예제 입력)
90

예제 출력)
90.00 kg =>  198.41 lb
'''

kg_number = float(input())
lb_number = 2.2046 * kg_number
print("%0.2f kg =>  %0.2f lb" %(kg_number, lb_number))