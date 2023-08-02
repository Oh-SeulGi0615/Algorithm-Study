import sys
input = sys.stdin.readline

for _ in range(int(input())):
    d, n, s, p = map(int, input().split())

    time_s = s * n
    time_p = p * n + d

    if time_p < time_s:
        print('parallelize')
    elif time_p > time_s:
        print('do not parallelize')
    else:
        print('does not matter')