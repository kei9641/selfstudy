# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 4

'''
다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
이 때 ["가위", "바위", "보"] 리스트를 활용합니다.

[입력]
두 줄에 ["가위", "바위", "보"] 중 하나가 차례로 주어진다.

[출력]
첫 번째 사람은 Man1, 두 번째 사람은 Man2라고 하고, 이긴 사람의 결과를 출력한다.
예를 들어, Man1이 이겼을 경우 Result : Man1 Win! 이라고 출력한다.
단, 비긴 경우는 Result : Draw 라고 출력한다.

예제 입력)
바위
가위

예제 출력)
Result : Man1 Win!
'''

# solution 1

rsp = ["가위", "바위", "보"]
Man1 = str(input())
Man2 = str(input())
if(Man1 == rsp[0]):
    if(Man2 == rsp[0]):
        print("Result : Draw")
    elif(Man2 == rsp[1]):
        print("Result : Man2 Win!")
    elif(Man2 == rsp[2]):
        print("Result : Man1 Win!")

elif(Man1 == rsp[1]):
    if(Man2 == rsp[0]):
        print("Result : Man1 Win!")
    elif(Man2 == rsp[1]):
        print("Result : Draw")
    elif(Man2 == rsp[2]):
        print("Result : Man2 Win!")

elif(Man1 == rsp[2]):
    if(Man2 == rsp[0]):
        print("Result : Man2 Win!")
    elif(Man2 == rsp[1]):
        print("Result : Man1 Win!")
    elif(Man2 == rsp[2]):
        print("Result : Draw")


# solution 2

rsp = ["가위", "바위", "보"]
man1 = str(input())
man2 = str(input())

if man1 == man2:
    print('Draw')
else:
    if (((man1 == rsp[0]) and (man2 == rsp[1])) or ((man1 == rsp[1]) and (man2 == rsp[2])) or ((man1 == rsp[2]) and (man2 == rsp[0]))):
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')