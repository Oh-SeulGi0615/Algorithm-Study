n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []

def back():
  if len(answer) == m:
    print(' '.join(map(str, answer)))
    return

  for i in arr:
    answer.append(i)
    back()
    answer.pop()

back()