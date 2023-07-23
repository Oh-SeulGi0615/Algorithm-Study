import sys
input = sys.stdin.readline

a = list(input().rstrip())

cnt = 1
for i in range(1, len(a)):
    if ord(a[i]) <= ord(a[i-1]):
        cnt += 1

print(cnt)