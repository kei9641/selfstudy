# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 4. 문자열 2

'''
다음과 같이 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하십시오. 

예제 입력)
A better tomorrow 

예제 출력)
tomorrow better A 
'''

# solution 1

words = input().split()
reverse = words[::-1]
for word in reverse:
    print(word, end=' ')


# solution 2

words = input().split()
words.reverse()
print(' '.join(words))