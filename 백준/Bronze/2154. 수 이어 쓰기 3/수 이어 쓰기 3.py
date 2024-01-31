import sys
input = sys.stdin.readline

n = int(input())

result = ''
for i in range(1, 100001):
    result += str(i)

print(len(result.split(str(n))[0]) + 1)