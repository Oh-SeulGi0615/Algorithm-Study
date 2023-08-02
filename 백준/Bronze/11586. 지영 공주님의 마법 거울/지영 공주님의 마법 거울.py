import sys
input = sys.stdin.readline

arr = [[input().rstrip()] for _ in range(int(input()))]

n = int(input())

if n == 1:
    for i in arr:
        print(i[0])
elif n == 2:
    for i in arr:
        print(i[0][::-1])
else:
    for i in arr[::-1]:
        print(i[0])