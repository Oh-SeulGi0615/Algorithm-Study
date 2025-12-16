import sys
input = sys.stdin.readline

t = int(input())

result = []
for i in range(5, 0, -1):
  a, b = divmod(t, 9**i)
  result.append(str(a))
  t = b
result.append(str(t))

print(int(''.join(result)))