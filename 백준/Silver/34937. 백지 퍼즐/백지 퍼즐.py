import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cnt = (n*(m-1)) + (m*(n-1))
print(3**cnt % (10**9+7))