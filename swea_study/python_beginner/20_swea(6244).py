# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 7

'''
다음은 학생의 점수를 나타내는 리스트입니다.
[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.

예제 출력)
454
'''

scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
score_sum = 0
idx = 0
while idx < len(scores):
    score = scores.pop(idx)
    if(score >= 80):
        score_sum = score_sum + score
print(score_sum)