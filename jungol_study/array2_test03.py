minus = [100]
minus.append(int(input()))
i = 0
while minus[i] - minus[i+1] >= 0:
    minus.append(minus[i] - minus[i+1])
    i += 1
minus.append(minus[i] - minus[i+1])
print(*minus)
