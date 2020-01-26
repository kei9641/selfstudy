# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 26

'''
두 개의 리스트 [1,3,6,78,35,55]와 [12,24,35,24,88,120,155]를 이용해
양쪽 리스트에 모두 있는 항목을 리스트로 반환하는 프로그램을 작성하십시오.

예제 출력)
[35] 
'''

list1 = [1,3,6,78,35,55]
list2 = [12,24,35,24,88,120,155]
result = list()
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            result.append(list1[i])
print(result)