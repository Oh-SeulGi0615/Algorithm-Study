import sys
input = sys.stdin.readline

while True:
    try:
        a, b, c = map(int, input().split())

        cnt = 0
        while True:
            if b - a == 1 and c - b == 1:
                break
            if b - a >= c - b:
                c = b - 1
                b, c = c, b
                cnt += 1
            elif b - a <= c - b:
                a = b + 1
                a, b = b, a
                cnt += 1
        print(cnt)
    except:
        break