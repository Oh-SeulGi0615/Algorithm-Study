import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(str(i)[::-1]) for i in range(n, n*k + 1, n)]

print(max(arr))