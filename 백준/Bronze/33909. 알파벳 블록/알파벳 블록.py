import sys

s, c, o, n = map(int, sys.stdin.readline().split())

result = min(((s + n) // 3), (c + (2 * o)) // 6)
print(result)