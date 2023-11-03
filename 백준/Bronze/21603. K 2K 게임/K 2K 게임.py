import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [i for i in range(1, n+1) if (i % 10 != k % 10) and (i % 10 != 2*k % 10)]

print(len(arr))
print(*arr)