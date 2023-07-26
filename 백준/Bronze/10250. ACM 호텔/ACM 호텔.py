import sys
input = sys.stdin.readline

a = int(input())
for _ in range(a):
    h, w, n = map(int, input().split())

    for i in range(1, w+1):
        for j in range(1, h+1):
            room = (j * 100) + i
            n -= 1
            if n == 0:
                print(room)
                break