import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = max(arr) + ((sum(arr) - max(arr)) / 2)
print(result)