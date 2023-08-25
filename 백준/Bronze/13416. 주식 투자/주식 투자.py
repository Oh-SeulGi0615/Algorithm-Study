import sys
input = sys.stdin.readline

for _ in range(int(input())):
    sum_ = 0
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        if max(a, b, c) >= 0:
            sum_ += max(a, b, c)
    print(sum_)