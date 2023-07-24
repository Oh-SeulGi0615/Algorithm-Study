import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    g = list(map(int, input().split()))
    s = list(map(int, input().split()))

    total1 = (g[0] * 1) + (g[1] * 2) + (g[2] * 3) + (g[3] * 3) + (g[4] * 4) + (g[5] * 10)
    total2 = (s[0] * 1) + (s[1] * 2) + (s[2] * 2) + (s[3] * 2) + (s[4] * 3) + (s[5] * 5) + (s[6] * 10)

    if total1 > total2:
        print(f'Battle {_+1}: Good triumphs over Evil')
    elif total1 < total2:
        print(f'Battle {_+1}: Evil eradicates all trace of Good')
    else:
        print(f'Battle {_+1}: No victor on this battle field')