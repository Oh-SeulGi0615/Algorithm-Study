import sys
input = sys.stdin.readline

for _ in range(int(input())):
    d = int(input())

    for i in range(d+1):
        t = i**2 + i
        if t > d:
            print(i-1)
            break