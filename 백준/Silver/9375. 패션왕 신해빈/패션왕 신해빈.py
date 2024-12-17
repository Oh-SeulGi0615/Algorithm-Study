for _ in range(int(input())):
  cnt = 1
  hash_table = {}
  for _ in range(int(input())):
    wear = input().split()
    if wear[1] not in hash_table:
      hash_table[wear[1]] = [None, wear[0]]
    else:
      hash_table[wear[1]].append(wear[0])
  
  for case in hash_table:
    cnt *= len(hash_table[case])
  
  print(cnt -1)