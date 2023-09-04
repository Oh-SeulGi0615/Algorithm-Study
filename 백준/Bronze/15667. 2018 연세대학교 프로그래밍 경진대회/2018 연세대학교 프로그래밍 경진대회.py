import sys
input = sys.stdin.readline

n = int(input())
for i in range(int(n ** 0.5)+1):
    if i ** 2 + i + 1 == n:
        print(i)
        break