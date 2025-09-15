n = int(input())
for i in range(n):
  charset = {chr(i): 0 for i in range(97, 123)}

  string = list(input().lower().replace(' ',''))
  for char in string:
    if char in charset:
      charset[char] += 1
  
  if min(charset.values()) == 0:
    print(f'Case {i+1}: Not a pangram')
  elif min(charset.values()) == 1:
    print(f'Case {i+1}: Pangram!')
  elif min(charset.values()) == 2:
    print(f'Case {i+1}: Double pangram!!')
  elif min(charset.values()) == 3:
    print(f'Case {i+1}: Triple pangram!!!')