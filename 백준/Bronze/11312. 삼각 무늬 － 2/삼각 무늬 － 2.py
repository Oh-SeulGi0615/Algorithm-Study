import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())

    print(int((a**2 / 2) / (b**2 / 2)))