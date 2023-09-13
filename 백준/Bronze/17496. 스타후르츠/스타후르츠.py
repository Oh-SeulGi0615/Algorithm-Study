import sys
input = sys.stdin.readline

n, t, c, p = map(int, input().split())

result = ((n-1) // t) * c * p
print(result)