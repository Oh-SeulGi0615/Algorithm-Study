import sys
input = sys.stdin.readline

n, l = map(int, input().split())
num = 1
while True:
    if n < 1:
        break
    if str(l) in str(num):
        num += 1
    else:
        num += 1
        n -= 1

print(num-1)