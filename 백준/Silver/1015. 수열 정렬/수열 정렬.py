import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

result = []
for i in a:
    result.append(b.index(i))
    b[b.index(i)] = -1

print(*result)