import sys
input = sys.stdin.readline

n = int(input())
arr = [2**i for i in range(31)]

if n in arr:
    print(1)
else:
    print(0)