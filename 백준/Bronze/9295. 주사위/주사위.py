import sys
input = sys.stdin.readline

for x in range(1, int(input())+1):
    a, b = map(int, input().split())

    print(f'Case {x}:', end=' ')
    print(a+b)