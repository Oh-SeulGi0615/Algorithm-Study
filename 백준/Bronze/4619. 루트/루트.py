import sys
input = sys.stdin.readline

while True:
    b, n = map(int, input().split())
    if b == 0 and n == 0:
        break

    x = int(b ** (1 / n))
    y = int(b ** (1 / n)) + 1

    if abs(b - (x ** n)) <= abs(b - (y ** n)):
        print(x)
    else:
        print(y)