# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 4. 문자열 4

'''
다음의 결과와 같이 여러 문장을 입력받아 대문자로 변환해 출력하는 프로그램을 작성합니다.
아무 것도 입력하지 않고 엔터만 입력하면 입력이 종료됩니다.

예제 입력)
Hello World
hello world
Python

예제 출력)
>> HELLO WORLD
>> HELLO WORLD
>> PYTHON
'''

sentences = list()
for i in range(3):
    sentence = input()
    if not sentence:
        break
    sentences.append(sentence)

for i in range(len(sentences)):
    print('>> {}' .format(sentences[i].upper()))


