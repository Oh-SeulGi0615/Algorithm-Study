import sys
input = sys.stdin.readline

n = input().rstrip()
f = int(input())

n_start = int(n[:-2] + '00')
n_end = int(n[:-2] + '99')

for i in range(n_start, n_end + 1):
    if i % f == 0:
        print(str(i)[-2:])
        break