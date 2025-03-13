n = int(input())

all_students = []
nominate = []
for _ in range(n):
  student = list(map(int, input().split()))
  all_students.append(student)

all_students = sorted(all_students, key = lambda x: -x[-1])

for i in all_students:
  if len(nominate) < 3:
    if nominate.count(i[0]) < 2:
      nominate.append(i[0])
      print(i[0], i[1])
    else:
      pass
  else:
    break