import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    arr = [0, 1]
    idx = 2
    while True:
        if idx > n:
            break
        arr.append(arr[-1] + arr[-2])
        idx += 1

    print(arr[-1])