# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 5. 연산자 1

'''
인치(inch)를 센티미터(cm)으로 변환하는 프로그램을 작성하십시오.
이 때 1 인치는 2.54 센티미터입니다. 

예제 입력)
3

예제 출력)
3.00 inch => 7.62cm
'''


inch_number = float(input())
cm_number = inch_number * 2.54
print("%0.2f inch =>  %0.2f cm" %(inch_number, cm_number))