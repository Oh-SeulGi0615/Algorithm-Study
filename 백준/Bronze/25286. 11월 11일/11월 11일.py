import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    y, m = map(int, input().split())

    month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        month[2] = 29

    if m == 1:
        print(y-1, 12, month[12])
    else:
        print(y, m-1, month[m-1])