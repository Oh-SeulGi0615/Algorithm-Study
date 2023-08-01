import sys
input = sys.stdin.readline

for _ in range(int(input())):

    sum1, sum2 = 0, 0
    for _ in range(int(input())):
        c, g = map(float, input().split())

        sum1 += int(c)
        sum2 += c * g

    print(sum1, round(sum2 / sum1, 1))