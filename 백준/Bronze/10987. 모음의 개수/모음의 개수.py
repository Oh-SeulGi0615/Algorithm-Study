import sys
input = sys.stdin.readline

a = input().rstrip()

b = ['a','e','i','o','u']

cnt = 0
for i in list(a):
    if i in b:
        cnt += 1

print(cnt)