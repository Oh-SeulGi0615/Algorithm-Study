n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []

def back():
  if len(answer) == m:
    print(' '.join(map(str, answer)))
    return

  for i in arr:
    if i not in answer and (not answer or answer[-1] <= i):
      answer.append(i)
      back()
      answer.pop()

back()