C, R = map(int, input().split())
shop = int(input())
position = []
for _ in range(shop):
    position.extend(list(map(int, input().split())))
Xdir, Xpos = map(int, input().split())
result = 0
if Xdir == 1:
    for i in range(0, len(position)-1, 2):
        if position[i] == 1:
            length = abs(Xpos - position[i+1])
        elif position[i] == 2:
            forward = C-Xpos + R + C-position[i+1]
            backward = Xpos + R + position[i+1]
            if forward > backward:
                length = backward
            else:
                length = forward
        elif position[i] == 3:
            length = Xpos + position[i+1]
        elif position[i] == 4:
            length = C-Xpos + position[i+1]
        result += length
elif Xdir == 2:
    for i in range(0, len(position)-1, 2):
        if position[i] == 2:
            length = abs(Xpos - position[i+1])
        elif position[i] == 1:
            forward = Xpos + R + position[i+1]
            backward = C-Xpos + R + C-position[i+1]
            if forward > backward:
                length = backward
            else:
                length = forward
        elif position[i] == 3:
            length = Xpos + R-position[i+1]
        elif position[i] == 4:
            length = C-Xpos + R-position[i+1]
        result += length
elif Xdir == 3:
    for i in range(0, len(position)-1, 2):
        if position[i] == 3:
            length = abs(Xpos - position[i+1])
        elif position[i] == 4:
            forward = Xpos + C + position[i+1]
            backward = R-Xpos + C + R-position[i+1]
            if forward > backward:
                length = backward
            else:
                length = forward
        elif position[i] == 1:
            length = Xpos + position[i+1]
        elif position[i] == 2:
            length = R-Xpos + position[i+1]
        result += length
elif Xdir == 4:
    for i in range(0, len(position)-1, 2):
        if position[i] == 4:
            length = abs(Xpos - position[i+1])
        elif position[i] == 3:
            forward = R-Xpos + C + R-position[i+1]
            backward = Xpos + C + position[i+1]
            if forward > backward:
                length = backward
            else:
                length = forward
        elif position[i] == 1:
            length = Xpos + C-position[i+1]
        elif position[i] == 2:
            length = R-Xpos + C-position[i+1]
        result += length
print(result)