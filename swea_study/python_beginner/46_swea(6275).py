# [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 2

'''
리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

예제 출력)
Pythn s pwrfl... nd fst; plys wll wth thrs; rns vrywhr; s frndly & sy t lrn; s Opn.
'''

delete = "aeiou"
sentence = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
result = [i for i in sentence if i not in delete]
print(''.join(result))