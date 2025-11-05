import sys

n = int(sys.stdin.readline())

month = 8 + (n - 1) * 7
y = 2024 + (month // 13)

if month % 12 == 0: m = 12
else: m = month % 12

print(y, m)