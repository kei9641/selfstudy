# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 5. 객체지향 2

'''
국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고
메서드를 호출하는 코드를 작성해봅시다.

예제 출력)
대한민국
대한민국
'''

class Korean:
    @staticmethod
    def printNationality():
        print('대한민국')
        
Korean.printNationality()
Korean.printNationality()