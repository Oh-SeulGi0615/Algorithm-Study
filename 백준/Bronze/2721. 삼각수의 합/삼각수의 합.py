import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    sum1 = 0
    for i in range(1, n+1):
        sum2 = 0
        for j in range(1, i+2):
            sum2 += j
        sum1 += i * sum2

    print(sum1)