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