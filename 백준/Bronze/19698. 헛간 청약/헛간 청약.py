import sys
input = sys.stdin.readline

n, w, h, l = map(int, input().split())

w2 = w // l
h2 = h // l

if (w2 * h2) > n:
    print(n)
else:
    print(w2*h2)