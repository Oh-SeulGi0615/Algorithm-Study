import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

sum = int(a / 2) + b

if sum >= n:
    print(n)
else:
    print(sum)