# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 13

'''
다음의 결과와 같이 10진수를 2진수로 변환하는 프로그램을 작성하십시오.

예제 입력)
9

예제 출력)
1001
'''
'''
.strip('') : 문자열에서 ''를 제거
'''

dec_num = int(input())
bin_num = bin(dec_num)
bin_string = str(bin_num)
print(bin_string.strip("0b"))