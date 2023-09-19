import sys
input = sys.stdin.readline

a, b = map(int, input().split())

x = (-1*2*a + ((2*a)**2 - (4*b))**0.5) / 2
y = (-1*2*a - ((2*a)**2 - (4*b))**0.5) / 2

if x > y:
    print(int(y), int(x))
elif x < y:
    print(int(x), int(y))
else:
    print(int(x))