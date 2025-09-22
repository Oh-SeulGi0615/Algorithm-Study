t = int(input())
for _ in range(t):
  n, a, b = map(int, input().split())

  bin_a = str(bin(a))[2:]
  bin_b = str(bin(b))[2:]

  print(bin_a.count('1') + bin_b.count('1') - 1)