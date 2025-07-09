import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

min_h, max_h = 0, max(trees)

while min_h <= max_h:
    height = (min_h + max_h) // 2

    cut = 0
    for tree in trees:
        if tree > height:
            cut += tree - height

    if cut < m:
        max_h = height - 1
    else:
        min_h = height + 1

print(max_h)