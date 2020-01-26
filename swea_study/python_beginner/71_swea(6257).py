# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 3. 자료구조 - 셋, 딕셔너리 5

'''
리스트의 원소를 키로 하고, 그 원소의 length를 값으로 갖는 딕셔너리 객체를 생성하는 코드를 작성해봅시다. 
이 때 딕셔너리 내포 기능을 사용하며, 원소의 공백은 제거합니다. 
리스트 fruit는 다음과 같습니다. fruit = ['   apple    ','banana','  melon'] 

예제 출력)
{'apple': 5, 'banana': 6, 'melon': 5} 
'''

fruit = ['   apple    ','banana','  melon'] 

result = {fruit[i].strip() : len(fruit[i].strip()) for i in range(len(fruit))}
print(result)