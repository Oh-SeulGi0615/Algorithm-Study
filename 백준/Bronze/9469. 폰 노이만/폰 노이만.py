import sys
input = sys.stdin.readline

p = int(input())
for _ in range(p):
    n, d, a, b, f = map(float, input().split())

    time = d / (a + b)
    distance = time * f
    
    print(int(n), end=' ')
    print(f'{distance:.6f}')