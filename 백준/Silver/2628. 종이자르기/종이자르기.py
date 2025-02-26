h, v = map(int, input().split())
h, v = [0, h], [0, v]

cut = int(input())
for _ in range(cut):
    a, b = map(int, input().split())
    if a == 0:
        v.append(b)
    else:
        h.append(b)

h.sort()
v.sort()

max_area = 0
for i in range(1, len(h)):
    for j in range(1, len(v)):
        area = (h[i] - h[i-1]) * (v[j] - v[j-1])
        if area > max_area:
            max_area = area
            
print(max_area)