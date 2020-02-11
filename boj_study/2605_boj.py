N = int(input())
sequence = list(map(int, input().split()))
students = []
for num in range(1, N+1):
    students.insert(num-1-sequence[num-1], num)
print(*students)
