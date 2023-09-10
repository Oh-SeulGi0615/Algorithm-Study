import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = n
group = n
while group > 1:
    a = group // m
    result += a
    group = a

print(result)