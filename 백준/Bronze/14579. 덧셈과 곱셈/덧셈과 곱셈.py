import sys
input = sys.stdin.readline

a, b = map(int, input().split())

answer = 1
for i in range(a, b+1):
    answer *= int((i * (i+1)) / 2)

print(answer % 14579)