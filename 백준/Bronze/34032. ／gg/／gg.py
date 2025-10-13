n = int(input())
votes = list(input())

count_o = votes.count('O')
if count_o >= (n / 2):
  print('Yes')
else:
  print('No')