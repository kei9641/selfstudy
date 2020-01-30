# 1번
'''
ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []

입력 예시)
ls = [0, 1, 3, 6, 10]

출력 예시)
[20, 20, 19, 16, 10, 0]
'''

# def parts_sums(numbers):
# 	sum_num = 0
# 	result = []
# 	lenth = len(numbers)
	
# 	for number in numbers: # 첫번째 값
# 		sum_num += number
# 	result.append(sum_num) 

# 	for _ in range(lenth):
# 		sum_num -= numbers.pop(0)
# 		result.append(sum_num)
# 	return result



# def parts_sums(numbers):
# 	sum_num = 0
# 	result = []

# 	while len(numbers) != 0:
# 		sum_num = 0
# 		for number in numbers: # 첫번째 값
# 			sum_num += number
# 		result.append(sum_num)
# 		numbers.pop(0) 
# 	result.append(0)

# 	return result



# def parts_sums(numbers):
# 	sum_num = 0
# 	numbers.reverse()
# 	result = [0]

# 	for number in numbers:		
# 		sum_num += number
# 		result.append(sum_num)

# 	return result[::-1]



# def parts_sums(numbers):
# 	result = []

# 	while len(numbers):
# 		result.append(sum(numbers))
# 		numbers = number[1:]
# 	result.append(0)
# 	return result




# def parts_sums(numbers):
# 	result = [sum(numbers)]

# 	for number in numbers:
# 		result.append(result[-1] - number)
# 	return result




# def parts_sums(numbers):
# 	result = [0]

# 	for idx, number in enumerate(numbers[::-1]):
# 		result += [number + result[idx]]
# 	return result[::-1]



# print(parts_sums([0, 1, 3, 6, 10])) 
# # [20, 20, 19, 16, 10, 0]
# print(parts_sums([1, 2, 3, 4, 5, 6])) 
# # [21, 20, 18, 15, 11, 6, 0]
# print(parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358])) 
# # [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]


# 2번

'''
Rh 식 혈액형은 사람의 혈액형 중 하나로서, ABO 식 혈액형 다음으로 중요한 혈액형으로 취급하고 있습니다. Rh 식 혈액형은 Rh+ 형과 Rh- 형으로 나누는데, 이 중 Rh+ 형이 대다수를 차지하며 전세계적으로 85% 정도가 Rh+ 형이고 나머지 15% 가량이 Rh- 형이라고 합니다.
입력으로 주어지는 데이터는 ABO 식 혈액형과 Rh 식 혈액형을 조합하여 표현한 문자열들로 이루어진 리스트입니다. 예를 들어, ABO 식으로는 A 형이면서 Rh+ 형인 사람의 혈액형은 "A+" 로 표현되는 방식입니다. 이러한 입력 데이터로부터, ABO 식 각 혈액형의 사람 수와 Rh 식 각 혈액형의 사람 수를 각각 집계하여 사전으로 반환하는 함수 bloodtype() 을 완성하세요. 사전을 이용할 때에는 키 (key) 의 유무에 주의하여 코드를 작성해야 합니다.
한 사람도 가지지 않는 혈액형에 대해서는 그 내용을 사전에 포함하지 않습니다. 즉, 값 (value) 이 0 인 키 (key) 는 사전에 담d지 않습니다.
예를 들어, 아래와 같은 입력이 주어질 때,
data = ['A+', 'B+', 'A-', 'O-', 'AB+', 'AB-']
올바른 리턴 값은 {'A': 2, '+': 3, 'B': 1, '-': 3, 'O': 1, 'AB': 2} 입니다.
'''
# def blood_type(blood):
# 	result = {}
# 	for bl in blood:
# 		if 'AB' in bl: 
# 			if 'AB' in result:
# 				result['AB'] += 1
# 			else:
# 				result['AB'] = 1
# 		else:
# 			for abo in abos:
# 				if abo in bl:
# 					if abo in result:
# 						result[abo] += 1
# 					else:
# 						result[abo] = 1
# 		for rh in rhs:
# 			if rh in bl:
# 				if rh in result:
# 					result[rh] += 1
# 				else:
# 					result[rh] = 1

# 	return result

# abos = ['A', 'B', 'O']
# rhs = ['+', '-']

def blood_type(blood):
	abos = ['AB', 'A', 'B', 'O', '+', '-']
	result = {}
	count = 0
	for abo in abos:
		for i in blood:
			if abo in i:
				count += 1
		if count == 0:
			continue
		result[abo] = count
		count = 0

	result['A'] -= result['AB']
	result['B'] -= result['AB']
			
	return result



print(blood_type(['A+', 'B+', 'A-', 'AB+', 'AB-'])) 
# {'A': 2, '+': 3, 'B': 1, '-': 3, 'O': 1, 'AB': 2}
