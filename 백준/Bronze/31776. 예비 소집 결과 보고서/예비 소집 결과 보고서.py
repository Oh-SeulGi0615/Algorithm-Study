cnt = 0
for _ in range(int(input())):
  q1, q2, q3 = map(int, input().split())

  if q1 >= 0 and (q1 <= q2):
    if q2 <= q3 or q3 == -1:
      cnt += 1
  elif q1 >= 0 and q2 == -1 and q3 == -1:
    cnt += 1

print(cnt)