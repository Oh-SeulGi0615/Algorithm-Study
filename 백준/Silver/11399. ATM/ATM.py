import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

cnt = 0
for i in range(1,n+1):
    cnt += sum(arr[:i])

print(cnt)