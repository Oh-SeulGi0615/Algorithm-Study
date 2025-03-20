n = int(input())
names = input().split()
p = {name:0 for name in names}

for _ in range(n):
  list_ = input().split()

  for name in list_:
    p[name] += 1

p = sorted([(v, p[v]) for k, v in enumerate(p)], key=lambda x: (-x[1], x[0]))
for i in p:
  print(i[0], i[1])