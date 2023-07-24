import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
x = input().rstrip()

for i in arr:
    if i == min(arr):
        a = i
    elif i == max(arr):
        c = i
    else:
        b = i

if x[0] == 'A':
    if x[1] == 'B':
        print(a, b, c)
    elif x[1] == 'C':
        print(a, c, b)
elif x[0] == 'B':
    if x[1] == 'A':
        print(b, a, c)
    elif x[1] == 'C':
        print(b, c, a)
elif x[0] == 'C':
    if x[1] == 'A':
        print(c, a, b)
    elif x[1] == 'B':
        print(c, b, a)