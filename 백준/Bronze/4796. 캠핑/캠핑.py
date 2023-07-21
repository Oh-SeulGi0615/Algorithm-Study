import sys
input = sys.stdin.readline

cnt = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    
    x, y = divmod(v, p)
    sum_ = (l * x) + min(l, y)
    print(f'Case {cnt}: {sum_}')
    cnt += 1