arr = []
for _ in range(int(input())):
  case_ = input()

  sum_ = 0
  for char in case_:
    if char.isdecimal() == True:
      sum_ += int(char)

  arr.append([len(case_), sum_, case_])

arr.sort(key=lambda x: (x[0], x[1], x[2]))
for i in arr:
  print(i[-1])