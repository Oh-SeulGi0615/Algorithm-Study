import sys
input = sys.stdin.readline

n = int(input())

cnt1, cnt2 = 0, 0
for _ in range(n):
    a, b = map(int, input().split())

    if a > b:
        cnt1 += 1
    elif a < b:
        cnt2 += 1

print(cnt1, cnt2)