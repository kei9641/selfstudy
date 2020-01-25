# [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 1

'''
다음의 결과와 같이 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고
그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.

예제 입력)
eye

예제 출력)
eye
입력하신 단어는 회문(Palindrome)입니다.
'''

# solution 1

a = input()
b = list(a)
c = list()

def rev():
    for i in reversed(range(len(b))):
        c.append(b[i])
    return c
        
x = rev()
for i in range(len(b)):
    print(c[i], end="")
if(x == c):
    print("\n입력하신 단어는 회문(Palindrome)입니다.")


# solution 2

def palindrome(words):
    is_palindrome = True
    for i in range(len(words) // 2):
        if words[i] != words[-1 - i]:
            is_palindrome = False
            break
    return is_palindrome

word = input()
result = palindrome(word)

if result == True:
    print("\n입력하신 단어는 회문(Palindrome)입니다.")


# solution 3

def palindrome(words):
    is_palindrome = False
    if words == words[::-1]:
        is_palindrome = True
    return is_palindrome

word = input()
result = palindrome(word)

if result == True:
    print("\n입력하신 단어는 회문(Palindrome)입니다.")
