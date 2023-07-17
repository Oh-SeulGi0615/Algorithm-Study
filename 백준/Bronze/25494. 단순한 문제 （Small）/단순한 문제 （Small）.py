import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    arr = []
    a, b, c = map(int, input().split())

    for x in range(1, a+1):
        for y in range(1, b+1):
            for z in range(1, c+1):
                if x % y == y % z and y % z == z % x:
                    arr.append((x, y, z))

    print(len(arr))