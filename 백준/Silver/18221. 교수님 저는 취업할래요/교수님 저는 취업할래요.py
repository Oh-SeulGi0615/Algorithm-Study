import math
n = int(input())
class_room = [list(map(int, input().split())) for _ in range(n)]

p, s = [0, 0], [0, 0]
others = []
can_resist = 0

for r in range(n):
    for c in range(n):
        now = class_room[r][c]
        if now == 5:
            p = [r, c]
        elif now == 2:
            s = [r, c]
        elif now == 1:
            others.append([r, c])

distance = math.sqrt(((max(p[0], s[0]) - min(p[0], s[0]))**2) + ((max(p[1], s[1]) - min(p[1], s[1]))**2))

if distance < 5:
    print(0)
else:
    for o in others:
        if max(p[0], s[0]) >= o[0] >= min(p[0], s[0]):
            if max(p[1], s[1]) >= o[1] >= min(p[1], s[1]):
                can_resist += 1
    if can_resist >= 3:
        print(1)
    else:
        print(0)