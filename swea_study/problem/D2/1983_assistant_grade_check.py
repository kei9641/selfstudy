T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    scores = [0] * N
    for i in range(N):
        middleScore, lastScore, subjectScore = map(int, input().split())
        totalScore = middleScore * 0.35 + lastScore * 0.45 + subjectScore * 0.2
        scores[i] = totalScore
    findGrade = scores[K-1]
    sortScore = list(sorted(scores))
    sortScore.reverse()

    result = ''
    start = 0
    end = int(N/10)
    for i in range(len(grade)):
        if sortScore[end-1] <= findGrade <= sortScore[start]:
            result = grade[i]
        start += int(N/10)
        end += int(N/10)
        if end >= N:
            break
    print('#{} {}'.format(tc+1, result))