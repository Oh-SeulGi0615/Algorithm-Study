import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = int(input())
    n = int(input())

    total = s
    if n > 0:
        for _ in range(n):
            a, b = map(int, input().split())
            total += a * b
    
    print(total)