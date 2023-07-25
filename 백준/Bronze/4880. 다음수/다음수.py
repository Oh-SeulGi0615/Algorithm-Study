import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    if b - a == c - b:
        d = b - a
        print(f'AP {c + d}')
        
    elif int(b / a) == int(c / b):
        d = int(b / a)
        print(f'GP {c * d}')