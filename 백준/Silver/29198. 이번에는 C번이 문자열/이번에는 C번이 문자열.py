import sys

m, n, k = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(m)]
arr = ''.join(sorted(list(''.join(sorted(arr)[:k]))))

print(arr)