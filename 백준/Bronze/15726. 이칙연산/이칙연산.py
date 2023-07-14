import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

answer1 = int((a * b) / c)
answer2 = int((a / b) * c)

print(max(answer1, answer2))