# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 4. 문자열 1

'''
다음의 결과와 같이 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오. 

예제 입력)
madam 

예제 출력)
madam
입력하신 단어는 회문(Palindrome)입니다.
'''

words = input()

if words == words[::-1]:
    print(words)
    print('입력하신 단어는 회문(Palindrome)입니다.')