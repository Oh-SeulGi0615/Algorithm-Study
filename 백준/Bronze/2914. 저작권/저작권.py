import sys
input = sys.stdin.readline

a, i = map(int, input().split())

x = a * (i - 1)
print(x + 1)