import sys
input = sys.stdin.readline

x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())

value1 = ((a // 3) * (x2 ** 3)) + (((b - d) // 2) * (x2 ** 2)) + ((c - e) * x2)
value2 = ((a // 3) * (x1 ** 3)) + (((b - d) // 2) * (x1 ** 2)) + ((c - e) * x1)

print(value1 - value2)