y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

diff = 0
al, ml = 0, 0

diff += (y2 * 360) + (m2 * 30) + d2
diff -= (y1 * 360) + (m1 * 30) + d1

ml = min(36, diff // 30)
for i in range(1, (diff // 360)+1):
  al += ((i-1) // 2) + 15

print(al, ml)
print(f'{diff}days')