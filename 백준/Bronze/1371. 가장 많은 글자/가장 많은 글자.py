char = {chr(i): 0 for i in range(97, 123)}

while True:
  try:
    arr = list(input().rstrip())
    for i in arr:
      if i != ' ':
        char[i] += 1
  except:
    break

max_char = max(list(char.values()))
max_char_arr = [i for i in list(char.keys()) if char[i] == max_char]
max_char_arr.sort()

print(*max_char_arr, sep='')