dwarfs = []
seven = []
for _ in range(9):
    dwarfs.append(int(input()))
for i1 in range(9):
    for i2 in range(i1+1, 9):
        for i3 in range(i2+1, 9):
            for i4 in range(i3+1, 9):
                for i5 in range(i4+1, 9):
                    for i6 in range(i5+1, 9):
                        for i7 in range(i6+1, 9):
                            if dwarfs[i1] + dwarfs[i2] + dwarfs[i3] + dwarfs[i4] + dwarfs[i5] + dwarfs[i6] + dwarfs[i7] == 100:
                                seven.append(dwarfs[i1])
                                seven.append(dwarfs[i2])
                                seven.append(dwarfs[i3])
                                seven.append(dwarfs[i4])
                                seven.append(dwarfs[i5])
                                seven.append(dwarfs[i6])
                                seven.append(dwarfs[i7])
result = seven[:7]
result.sort()
for j in range(7):
    print(result[j])