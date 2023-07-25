import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())

basket = [i for i in range(1,m+1)]

cnt = 0
for _ in range(j):
    a = int(input())

    while True:
        if a in basket:
            break
        else:
            if basket[-1] < a:
                basket = list(map(lambda x: x+1, basket))
                cnt += 1
            elif basket[0] > a:
                basket = list(map(lambda x: x-1, basket))
                cnt += 1

print(cnt)