n, m = map(int, input().split())

string = list(input())
chars = [0 for _ in range(26)]
delete_count = [0 for _ in range(26)]

for char in string:
  chars[ord(char)-97] += 1

for i in range(len(chars)):
  if m != 0:
    if m >= chars[i]:
      delete_count[i] = chars[i]
      m -= chars[i]
    else:
      delete_count[i] = m
      m = 0
      break
  else:
    break

result = ''
for char in string:
  if delete_count[ord(char)-97] > 0:
    delete_count[ord(char)-97] -= 1
  else:
    result += char

print(result)