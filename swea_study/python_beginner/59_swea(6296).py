# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 19

'''
단어를 콤마(,)로 구분해 입력하면 그 단어들을 사전순으로 정렬해 출력하는 프로그램을 작성하시시오.

예제 입력)
python, hello, world, hi

예제 출력)
hello, hi, python, world 
'''

words = input().split(', ')
words.sort()

for i in range(len(words)-1):
    print(words[i], end=', ')
print(words[-1])