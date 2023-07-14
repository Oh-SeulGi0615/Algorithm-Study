import sys
input = sys.stdin.readline

a, o1, o2 = map(int, input().split())

x1 = a - o1
x2 = a - o2

print((min(o1, o2) + min(x1, x2)))