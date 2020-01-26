# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 21

'''
주어진 튜플 (1,2,3,4,5,6,7,8,9,10)의 앞 항목 절반과 뒤 항목 절반을 출력하는 프로그램을 작성하십시오. 

예제 출력)
(1, 2, 3, 4, 5)
(6, 7, 8, 9, 10)
'''

oneTuple = (1,2,3,4,5,6,7,8,9,10)
middle = int(len(oneTuple) / 2)
half1 = oneTuple[:middle]
half2 = oneTuple[middle:]
print(half1)
print(half2)