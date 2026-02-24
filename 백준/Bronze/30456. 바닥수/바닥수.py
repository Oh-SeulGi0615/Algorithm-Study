import sys
input = sys.stdin.readline

n, l = map(int, input().split())

res = '1' * (l-1) + str(n)
print(res)