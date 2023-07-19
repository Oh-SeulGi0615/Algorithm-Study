import sys
input = sys.stdin.readline

n = int(input())

plug = 1
for _ in range(n):
    a = int(input())

    plug += a - 1

print(plug)