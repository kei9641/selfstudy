N = int(input())
result = 0
for _ in range(N):
    words = list(input())
    stack = []
    if len(words) % 2 == 0:
        for word in words:
            if len(stack) and stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
        if not stack:
            result += 1

print(result)
