# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 6

'''
다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

예제 출력)
{'A': 3, 'O': 3, 'B': 2, 'AB': 2} 
'''

# solution 1

student = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
a = 0
b = 0
c = 0
d = 0
for i in range(len(student)):
    if(student[i] == 'A'):
        a = a + 1
    elif(student[i] == 'B'):
        b = b + 1
    elif(student[i] == 'O'):
        c = c + 1
    elif(student[i] == 'AB'):
        d = d + 1

print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d} " %(a, c, b, d)) 


# solution 2

dic = {}
students_blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

for blood in students_blood:
    if blood not in dic:
        dic[blood] = 1
    else:
        dic[blood] += 1
print(dic)


# solution 3

dic = {}
students_blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

for blood in students_blood:
    dic[blood] = students_blood.count(blood)
print(dic)


# solution 4

dic = {}

for blood in students_blood:
    dic[blood] = dic.get(blood, 0) + 1
print(dic)