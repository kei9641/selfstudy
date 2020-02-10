T = int(input())
for tc in range(T):
    quiz = input()
    count = 0
    score = 0
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            count += 1
        else:
            count = 0
        score += count
    print(score)