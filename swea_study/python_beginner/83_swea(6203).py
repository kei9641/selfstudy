# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 5. 객체지향 1

'''
다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오. 
이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.

예제 입력)
89, 90, 100 

예제 출력)
국어, 영어, 수학의 총점: 279 
'''

class student:
    def __init__(self, kor, eng, mat):
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        
    def get_total(self):
        return self.__kor + self.__eng + self.__mat
    
score = input().split(', ')
scores = list(map(int, score))
result = student(scores[0], scores[1], scores[2])
print('국어, 영어, 수학의 총점: {}' .format(result.get_total()))