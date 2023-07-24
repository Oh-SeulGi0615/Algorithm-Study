import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    a = list(bin(n))[2:][::-1]
    for i in range(len(a)):
        if a[i] == '1':
            print(i, end=' ')