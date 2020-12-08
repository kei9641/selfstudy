active = list(input())
bar = 0
result = 0

i = 0
while i < len(active):
    if active[i] == '(':
        if active[i+1] == ')':
            result += bar
            i += 1
        else:
            bar += 1
            result += 1
    else:
        bar -= 1
    i += 1

print(result)