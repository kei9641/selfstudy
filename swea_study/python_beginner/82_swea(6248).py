# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 4. 문자열 7

'''
다음 결과와 같이 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는 프로그램을 작성하십시오. 

예제 입력)
H1e2l3l4o5w6o7r8l9d

예제 출력)
Helloworld 
'''

words = input()
result = ''
for idx in range(len(words)):
    if idx % 2 == 0:
        result += words[idx]
print(result)