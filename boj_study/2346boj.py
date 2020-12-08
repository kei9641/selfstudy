from collections import deque

N = int(input())
numbers = list(map(int, input().split()))

balloons = deque()
for i in range(N):
    balloons.append((numbers[i], i+1))

while balloons:
    number, balloon = balloons.popleft()
    print(balloon)
    if number > 0:
        balloons.rotate(-(number)+1)
    else:
        balloons.rotate(-number)
