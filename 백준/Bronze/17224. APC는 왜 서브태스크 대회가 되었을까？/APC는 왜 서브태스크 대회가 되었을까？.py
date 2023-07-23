import sys
input = sys.stdin.readline

n, l, k = map(int, input().split())

easy, hard = [], []
point = 0

for _ in range(n):
    a, b = map(int, input().split())
    if b <= l:
        point += 140
        k -= 1
        if k == 0:
            break
    else:
        easy.append(a)

for i in range(k):
    if easy[i] <= l:
        point += 100

print(point)    