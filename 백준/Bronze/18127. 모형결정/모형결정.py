import sys
input = sys.stdin.readline

a, b = map(int, input().split())

total = 1
for i in range(1, b+1):
    sub = 1+(a-2)*i
    total += sub

print(total)