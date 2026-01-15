import sys
input = sys.stdin.readline

char_set = {'A':'a', 'B':'v', 'E':'ye', 'K':'k', 'M':'m', 'H':'n', 'O':'o', 'P':'r', 'C':'s', 'T':'t', 'Y':'u', 'X':'h'}

string = list(input().rstrip())

res = ''
for char in string:
  res += char_set[char]

print(res)