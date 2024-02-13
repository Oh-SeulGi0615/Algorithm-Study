import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
    
def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

for _ in range(int(input())):
    parent = dict()
    number = dict()

    for _ in range(int(input())):
        a, b = map(str, input().split())

        if a not in parent:
            parent[a] = a
            number[a] = 1

        if b not in parent:
            parent[b] = b
            number[b] = 1

        union(a, b)
        print(number[find(a)])