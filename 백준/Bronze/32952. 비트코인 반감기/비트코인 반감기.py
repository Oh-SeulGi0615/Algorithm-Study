import sys

r, k, m = map(int, sys.stdin.readline().rstrip().split())

cnt = m // k
result = r * (1/2)**cnt
print(int(result))