import sys

n = int(sys.stdin.readline())
divide_char = list(sys.stdin.readline().split())

m = int(sys.stdin.readline())
divide_num = list(map(int, sys.stdin.readline().split()))
divide = divide_char + divide_num

k = int(sys.stdin.readline())
combine = list(sys.stdin.readline().split())

s = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

for i in divide:
  if str(i) not in combine:
    string = string.replace(str(i), ' ')

print(*string.split(), sep='\n')