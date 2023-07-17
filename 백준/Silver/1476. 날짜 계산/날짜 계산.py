import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())

a, b, c, cnt = 1, 1, 1, 1
while True:
    if a == e and b == s and c == m:
        print(cnt)
        break

    a += 1
    b += 1
    c += 1

    if a > 15:
        a -= 15
    if b > 28:
        b -= 28
    if c > 19:
        c -= 19
    
    cnt += 1