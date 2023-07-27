import sys
input = sys.stdin.readline

b, c, d = map(int, input().split())
burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

burger.sort()
side.sort()
drink.sort()

burger = burger[::-1]
side = side[::-1]
drink = drink[::-1]

min_ = min(b, c, d)
sum_ = sum(burger) + sum(side) + sum(drink)
print(sum_)

for i in range(min_):
    sum_ -= int(burger[i] * 0.1) + int(side[i] * 0.1) + int(drink[i] * 0.1)

print(sum_)