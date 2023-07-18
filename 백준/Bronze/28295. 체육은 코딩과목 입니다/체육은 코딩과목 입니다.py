import sys
input = sys.stdin.readline

now = 'N'
for _ in range(10):
    t = int(input())

    if t == 1:
        if now == 'N':
            now = 'E'
        elif now == 'E':
            now = 'S'
        elif now == 'S':
            now = 'W'
        elif now == 'W':
            now = 'N'
    
    elif t == 2:
        if now == 'N':
            now = 'S'
        elif now == 'E':
            now = 'W'
        elif now == 'S':
            now = 'N'
        elif now == 'W':
            now = 'E'
    
    else:
        if now == 'N':
            now = 'W'
        elif now == 'E':
            now = 'N'
        elif now == 'S':
            now = 'E'
        elif now == 'W':
            now = 'S'

print(now)