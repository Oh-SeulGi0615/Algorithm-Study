import sys
input = sys.stdin.readline

n = int(input())

changes = 1000 - n

a, x = divmod(changes, 500)
b, x = divmod(x, 100)
c, x = divmod(x, 50)
d, x = divmod(x, 10)
e, x = divmod(x, 5)

print(a+b+c+d+e+x)