import sys
input = sys.stdin.readline

n, l, k = map(int, input().split())

easy, hard = [], []
for _ in range(n):
    a, b = map(int, input().split())
    easy.append(a)
    hard.append(b)

point = 0
for i in range(k):
    if easy[i] <= l and hard[i] > l:
        point += 100
    elif easy[i] <= l and hard[i] <= l:
        point += 140

print(point)