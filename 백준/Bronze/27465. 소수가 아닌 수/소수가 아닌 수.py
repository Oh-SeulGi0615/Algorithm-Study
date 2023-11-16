import sys
input = sys.stdin.readline

n = int(input())

if n * 4 >= 10 ** 9:
    print(10 ** 9)
else:
    print(n * 4)