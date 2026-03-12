import sys
input = sys.stdin.readline

p_a = list(map(int, input().split()))
p_b = list(map(int, input().split()))

cnt = 0
if (p_a[0] == 0 and p_b[0] == 0 and p_b[1] < p_a[1]) or (p_a[1] == 0 and p_b[1] == 0 and p_b[0] < p_a[0]):
  cnt = 3
elif p_a[0] == 0 or p_a[1] == 0:
  cnt = 1
else:
  cnt = 2

print(cnt)