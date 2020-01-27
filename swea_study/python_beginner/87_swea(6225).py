# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 5. 객체지향 5

'''
가로, 세로 정보을 갖고, 사각형의 면적을 계산하는 메서드를 갖는 Rectangle 클래스를 정의하고,
생성한 객체의 사각형의 면적을 출력하는 프로그램을 작성하십시오.

예제 출력)
사각형의 면적: 20 
'''

class Rectangle:
    def __init__(self, width, high):
        self.__width = width
        self.__high = high
    def get_area(self):
        return self.__width * self.__high
    
rectangle = Rectangle(4, 5)
print('사각형의 면적: {}' .format(rectangle.get_area()))