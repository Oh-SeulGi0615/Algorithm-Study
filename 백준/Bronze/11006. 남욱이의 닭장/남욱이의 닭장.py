import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())

    leg = m * 2
    print(leg - n, end=' ')
    print(m - (leg - n))