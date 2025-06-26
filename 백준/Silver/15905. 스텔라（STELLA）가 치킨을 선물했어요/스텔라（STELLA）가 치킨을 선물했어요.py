n = int(input())

result = 0
if n  == 5:
  print(result)
else:
  arr = []
  for _ in range(n):
    s, p = map(int, input().split())
    arr.append((s, p))
  
  arr = sorted(arr, key=lambda x: (-x[0], x[1]))
  fifth_score = arr[:5][-1][0]
  unlanked = [comp for comp in arr[5:] if comp[0] == fifth_score]

  print(len(unlanked))