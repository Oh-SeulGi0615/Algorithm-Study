import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
for _ in range(9):
    a = int(input())
    cnt += a

print(n - cnt)