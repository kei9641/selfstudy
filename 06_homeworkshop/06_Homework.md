# 06_Homework

> 1. Python은 객체 지향 프로그래밍 언어입니다. Python에서 기본적으로 정의되어 있는 클래스 5가지만 작성하시오.

- str()
- list()
- dict()
- int()
- print()



> 2. 다음 매직 메서드의 역할을 간단하게 작성하시오.

- `__init__` : 
- `__del__` : 
- `__str__` : 
- `__repr__` : 



> 3. 아래 코드의 **'.sort()'**와 같이 문자열, 리스트, 딕셔너리 등을 조작할 때 사용하였던 것들은 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드 3가지를 그 력할과 함께 작성하시오.

```python
numbers = [5, 1, 2]
numbers.sort()
print(numbers) # [1, 2, 5]
```

```python
#1. upper : 문자열을 대문자로 변환
string = 'abcdef'
print(string.upper()) # 'ABCDEF'

#2. append : 리스트의 마지막에 요소 추가
numbers = [1, 2, 3, 4, 5]
numbers.append(0)
print(numbers) # [1, 2, 3, 4, 5, 0]

#3. values : 딕셔너리의 value 값을 반환
dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}
for val in dictionary.values():
    print(val) # 1
    		   # 2
        	   # 3
```

