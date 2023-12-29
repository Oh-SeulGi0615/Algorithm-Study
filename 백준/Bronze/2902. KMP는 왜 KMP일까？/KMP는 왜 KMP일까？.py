import sys
input = sys.stdin.readline

arr = list(input().split('-'))

result = ''
for i in arr:
    result += i[0]

print(result)