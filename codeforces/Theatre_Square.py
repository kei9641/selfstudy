n, m, a = map(int, input().split())
row = n // a
column = m // a
if n != row * a:
    row += 1
if m != column * a:
    column += 1
print(row*column)