import sys
input = sys.stdin.readline

n = int(input())
string = input().rstrip()

rev_string = string[::-1]

res = ''
for i in range(n):
  if string[i] == rev_string[i] != '?':
    res += string[i]
  elif string[i] != '?' and rev_string[i] == '?':
    res += string[i]
  elif string[i] == '?' and rev_string[i] != '?':
    res += rev_string[i]
  else:
    res += 'a'

print(res)