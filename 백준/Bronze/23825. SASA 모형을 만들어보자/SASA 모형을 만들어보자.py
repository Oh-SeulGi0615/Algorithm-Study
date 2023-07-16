import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if a <= b:
    print(a // 2)
else:
    print(b // 2)