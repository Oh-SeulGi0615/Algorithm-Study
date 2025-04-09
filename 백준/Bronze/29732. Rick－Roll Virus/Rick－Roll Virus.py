n, m, k = map(int, input().split())
state = list(input())
r_location = [i for i in range(len(state)) if state[i] == 'R']

for location in r_location:
  for i in range(max(location-k, 0), min(n, location + k + 1)):
    state[i] = 'R'

if state.count('R') <= m:
  print('Yes')
else:
  print('No')