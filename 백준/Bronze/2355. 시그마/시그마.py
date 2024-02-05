import sys
input = sys.stdin.readline

a, b = map(int, input().split())

c, d = min(a, b), max(a, b)
result = ((c + d) * (d - c + 1)) // 2

print(result)