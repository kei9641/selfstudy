# def dfs(string):
#     global A, B, C, D
#     for num in range(2):
#         binary.append(num)
#         if '00' == str(binary[-2]) + str(binary[-1]):
#             if A > 0:
#                 A -= 1
#         elif '01' == str(binary[-2]) + str(binary[-1]):
#             if B > 0:
#                 B -= 1
#         elif '10' == str(binary[-2]) + str(binary[-1]):
#             if C > 0:
#                 C -= 1
#         elif '11' == str(binary[-2]) + str(binary[-1]):
#             if D > 0:
#                 D -= 1



# T = int(input())
# for tc in range(T):
#     A, B, C, D = map(int, input().split())
#     binary = []
#     for num in range(2):
#         binary.append(num)
#         dfs(binary)
#         if A+B+C+D+1 == len(binary):
#             break
#         binary.clear()
#     if A+B+C+D+1 != len(binary):
#         print('impossible')
#     else:
#         for i in range(len(binary)):
#             print(binary[i], end='')
#     print()
a = 1
b = 1
c = 1
if a == b == c:
    print('f')