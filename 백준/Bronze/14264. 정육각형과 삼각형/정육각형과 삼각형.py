import sys
input = sys.stdin.readline

n = int(input())

answer = n * (3 ** 0.5) * (n / 2) * 0.5
print(answer)