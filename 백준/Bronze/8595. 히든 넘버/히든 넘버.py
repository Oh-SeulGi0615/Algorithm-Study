n = int(input())
string = list(input())

num = 0
sub = ''
is_num = False
for i in string:
  if i.isdigit() == True:
    if len(sub) < 6:
      sub += i
    else:
      num += int(sub)
      sub = i

  else:
    if sub:
      num += int(sub)
      sub = ''
if sub:
  num += int(sub)

print(num)