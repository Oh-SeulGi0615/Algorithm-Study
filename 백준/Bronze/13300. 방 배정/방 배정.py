import sys
input = sys.stdin.readline

n, k = map(int, input().split())

member = [[] for _ in range(7)]
for _ in range(n):
    s, y = map(int, input().split())
    member[y].append(s)

room = 0
for i in member:
    g = i.count(0)
    b = i.count(1)
    
    g1, g2 = divmod(g, k)
    b1, b2 = divmod(b, k)

    room += g1 + b1
    if g2 > 0:
        room += 1
    if b2 > 0:
        room += 1

print(room)