alphabets = input()
for i in range(len(alphabets)):
    print(ord(alphabets[i]) - ord('A') + 1, end=' ')