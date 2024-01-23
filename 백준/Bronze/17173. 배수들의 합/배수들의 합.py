import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = [i for i in range(1, n+1) for j in arr if i % j == 0]

print(sum(list(set(result))))