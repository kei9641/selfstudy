# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 5. 객체지향 6

'''
Shape를 부모 클래스로 Square 자식 클래스를 정의하는 코드를 작성하십시오.
Square 클래스는 length 필드를 가지며, 0을 반환하는 Shape 클래스의 area 메서드를
length * length 값을 반환하는 메서드로 오버라이딩합니다.

예제 출력)
정사각형의 면적: 9 
'''

class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        self.__length = length
 
    def area(self):
        return self.__length ** 2

square = Square(3)
print("정사각형의 면적: {}".format(square.area()))
