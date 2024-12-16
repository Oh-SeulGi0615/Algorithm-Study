for _ in range(int(input())):
  charset = {chr(i):0 for i in range(97, 123)}
  first, second = map(str, input().split())

  if len(first) == len(second):
    for i in range(len(first)):
      charset[first[i]] += 1
      charset[second[i]] -= 1

    if len(list(set(list(charset.values())))) > 1:
      print('Impossible')
    else:
      print('Possible')
  else:
    print('Impossible')