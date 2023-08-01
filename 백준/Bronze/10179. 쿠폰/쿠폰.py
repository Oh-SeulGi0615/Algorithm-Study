import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = float(input())

    result = round(n * 0.8, 2)
    print(f'${result:.2f}')