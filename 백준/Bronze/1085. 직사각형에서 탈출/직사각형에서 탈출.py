x, y, w, h = map(int, input().split())

distance = []

a, b, c, d = x, y, w-x, h-y

distance.append(a)
distance.append(b)
distance.append(c)
distance.append(d)

print(min(distance))