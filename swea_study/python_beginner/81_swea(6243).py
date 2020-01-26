# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 4. 문자열 5

'''
사용자가 입력한 문장에서 공백을 이용해 단어들을 구분하고, 
중복된 단어없이 단어를 콤마(,)로 구분해 사전순으로 출력하는 프로그램을 작성하십시오. 

예제 입력)
산 하늘 강 바다 하늘 강 들 

예제 출력)
강,들,바다,산,하늘
'''

words = input().split()
result = list(set(words))
result.sort()
for i in range(len(result)-1):
    print(result[i], end=',')
print(result[-1])