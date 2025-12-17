import sys
input = sys.stdin.readline

h1, h2, h3 = map(int, input().split())
n = int(input())

a, b = divmod(n, 2)
result = (a * ((2 * h3) + h2)) + (b * (h1 + h2 + h3))

print(result)