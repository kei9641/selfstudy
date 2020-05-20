def solution(s):
    answer = []
    powersets = []
    mark = '{}'
    turn = 1
    
    # 부분집합 구분
    strings = list(s.split('},'))
    
    for string in strings:
        words = ''
        # {}제거
        for word in string:
            if word not in mark:
                words += word
        # 원소 나누기
        powersets.append(list(map(int, words.split(','))))
    # 원소가 적은 순서대로 부분집합의 원소 추가
    while len(powersets)+1 != turn:
        for powerset in powersets:
            if turn == len(powerset):
                # answer에 추가되지 않은 원소라면 추가
                for num in powerset:
                    if num not in answer:
                        answer.append(num)
                turn += 1
    
    return answer