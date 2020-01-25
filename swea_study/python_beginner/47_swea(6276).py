# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 3

'''
다음의 결과와 같이 구구단 2단부터 9단의 결과값 중에 3의 배수거나 7의 배수인 수를
제외한 값을 리스트 객체 result 안에 각 단마다 리스트를 만들어 삽입하고 이를 출력하십시오.

예제 출력)
[[2, 4, 8, 10, 16], [], [4, 8, 16, 20, 32], [5, 10, 20, 25, 40], [], [], [8, 16, 32, 40, 64], []]
'''

result = []
for i in range(2, 10):
    multi = []
    for j in range(1, 10):
        x = i * j
        if not (x % 3) or not (x % 7):
            continue
        multi.append(x)
    result.append(multi)
print(result)