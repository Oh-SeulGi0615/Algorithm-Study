n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

cnt = {i: arr.count(i) for i in arr}
answer, saved = [], {}

def back():
  if len(answer) == m:
    string = ' '.join(map(str, answer))
    if string not in saved:
      print(string)
      saved[string] = False
    return 

  for i in arr:
    answer.append(i)
    back()
    answer.pop()

back()