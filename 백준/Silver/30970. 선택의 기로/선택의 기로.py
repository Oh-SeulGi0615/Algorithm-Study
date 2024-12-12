import itertools
arr = [list(map(int, input().split())) for _ in range(int(input()))]

method1 = sorted(arr, key=lambda x: (-x[0], x[1]))[:2]
method2 = sorted(arr, key=lambda x: (x[1], -x[0]))[:2]

print(*list(itertools.chain.from_iterable(method1)))
print(*list(itertools.chain.from_iterable(method2)))