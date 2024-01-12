import sys
input = sys.stdin.readline

e, f, c = map(int, input().split())

drink = 0
bottle = e + f
while True:
    if bottle < c:
        break
    bottle -= c - 1
    drink += 1

print(drink)