# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 7. 흐름과 제어 - 반복 10

'''
다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.

예제 입력)
11

예제 출력)
0 1 2 3 4 5 6 7 8 9
0 2 0 0 0 0 0 0 0 0
'''

# solution 1

n = input()
m = []
num = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(n)):
    m.append(n[i])
for i in m:    
    for j in range(9):
        if int(i) == j:
            num[j] += 1
print("0 1 2 3 4 5 6 7 8 9")
print(" ".join(map(str, num)))


# solution 2

dic = {}
number = list(input())
keys = list()
values = list()

for i in range(10):
    dic[i] = 0
for i in range(len(number)):
    dic_number = int(number[i])
    dic[dic_number] += 1

for key, val in dic.items():
    keys.append(key)
    values.append(val)

for i in range(len(keys)):
    print(keys[i], end=' ')
print()
for i in range(len(values)):
    print(values[i], end=' ')