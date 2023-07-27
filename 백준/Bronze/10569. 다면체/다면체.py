import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    v, e = map(int, input().split())

    a = 2 - v + e
    print(a)