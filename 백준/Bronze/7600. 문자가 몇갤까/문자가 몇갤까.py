import sys
input = sys.stdin.readline

while True:
  string = input().rstrip()
  if string == '#':
    break

  char_set = set()
  for char in string.lower():
    if char.isalpha():
      char_set.add(char)
  
  print(len(char_set))