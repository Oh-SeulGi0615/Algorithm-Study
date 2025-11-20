import sys
input = sys.stdin.readline

n = int(input())
for num in range(n, 0, -1):
  if list(set(map(int, list(str(num))))) in [[4], [7], [4, 7], [7, 4]]:
    print(num)
    break