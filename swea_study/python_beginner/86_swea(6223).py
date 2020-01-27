# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 5. 객체지향 4

'''
반지름 정보를 갖고, 원의 면적을 계산하는 메서드를 갖는 Circle 클래스를 정의하고,
생성한 객체의 원의 면적을 출력하는 프로그램을 작성하십시오.

예제 출력)
원의 면적: 12.56 
'''

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_area(self):
        return 3.14 * self.__radius * self.__radius

circle = Circle(2)
print('원의 면적: {}' .format(circle.get_area()))