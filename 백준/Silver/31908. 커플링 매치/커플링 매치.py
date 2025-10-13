n = int(input())

rings = {}
couples = []
for _ in range(n):
  name, ring = input().split()
  if ring == '-':
    continue

  if ring not in rings:
    rings[ring] = []
  rings[ring].append(name)

for i in rings.values():
  if len(i) == 2:
    couples.append(i)

print(len(couples))
if len(couples) > 0:
  for couple in couples:
    print(*couple)