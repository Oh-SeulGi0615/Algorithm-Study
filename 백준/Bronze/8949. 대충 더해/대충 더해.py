import sys
input = sys.stdin.readline

num1, num2 = map(str, input().rstrip().split())
num1 = num1.zfill(max(len(num1), len(num2)))
num2 = num2.zfill(max(len(num1), len(num2)))

res = ''
for i in range(len(num1)):
  res += str(int(num1[i]) + int(num2[i]))

print(res)