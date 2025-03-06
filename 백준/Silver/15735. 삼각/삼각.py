n = int(input())

result = 0
for i in range(1, n+1):
  result += sum(range(1, (n-i)+2))
  result += sum(range(1, (n-(2*i))+2))

print(result)