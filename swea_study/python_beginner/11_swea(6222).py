# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 5

'''
다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,
알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
출력 시 아스키코드를 함께 출력합니다.

예제 입력)
c

예제 출력)
c(ASCII: 99) => C(ASCII: 67)
'''
'''
.islower() : 문자열이 모두 소문자이면 True
.upper() : 문자열을 모두 대문자로 변환
ord() : 문자의 아스키코드 값을 반환
chr() : 숫자에 해당하는 아스키코드 문자를 반환
'''

# solution 1

i = str(input())

if((i >= "a") and (i <= "z")): #.islower()
    a = ord(i)
    b = ord(i) - ord("a") + ord("A")
    j = chr(b)
    '''
    ord() chr()
    temp = lower(i)
    print(temp)
'''
    print("%s(ASCII: %d) => %s(ASCII: %d)" %(i, a, j, b)) 
elif((i >= "A") and (i <= "Z")):
    a = ord(i)
    b = ord(i) - ord("A") + ord("a")
    j = chr(b)
    print("%s(ASCII: %d) => %s(ASCII: %d)" %(i, a, j, b)) 
else:
    print(i)


# solution 2

input_string = input()

if input_string.islower():
    change_string = input_string.upper()
    inaskii_number = ord(input_string)
    chaskii_number = ord(change_string)
    print("%s(ASCII: %d) => %s(ASCII: %d)" %(input_string, inaskii_number, change_string, chaskii_number))
elif input_string.isupper():
    change_string = input_string.lower()
    inaskii_number = ord(input_string)
    chaskii_number = ord(change_string)
    print("%s(ASCII: %d) => %s(ASCII: %d)" %(input_string, inaskii_number, change_string, chaskii_number))
else:
    print(input_string)
