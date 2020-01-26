# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 4. 문자열 3

'''
다음의 결과와 같이 임의의 URL 주소를 입력받아 protocol, host, 나머지(path, querystring, ...)로
구분하는 프로그램을 작성하십시오.

예제 입력)
http://www.example.com/test?p=1&q=2 

예제 출력)
protocol: http
host: www.example.com
others: test?p=1&q=2
'''

url = input().split('/')
divide_url = {}

divide_url['protocol'] = url[0].strip(':')
divide_url['host'] = url[2]
divide_url['others'] = url[3]

for key, value in divide_url.items():
    print('{}: {}' .format(key, value))