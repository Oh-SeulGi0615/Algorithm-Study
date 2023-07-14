import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

t = int(c / (a*2))
print(b*t)