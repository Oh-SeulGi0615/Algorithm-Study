import sys

n = int(sys.stdin.readline())

space = []
head = []
heart = []
for i in range(n):
  arr = list(sys.stdin.readline().rstrip())
  space.append(arr)
  if not head and arr.count('*') == 1:
    head = [i, arr.index('*')]
    heart = [head[0]+1, head[1]]

left_arm = space[heart[0]][:heart[1]].count('*')
right_arm = space[heart[0]][heart[1]+1:].count('*')
waist = [space[i][heart[1]] for i in range(heart[0]+1, len(space))]
left_leg = [space[i][heart[1]-1] for i in range(heart[0]+waist.count('*')+1, len(space))].count('*')
right_leg = [space[i][heart[1]+1] for i in range(heart[0]+waist.count('*')+1, len(space))].count('*')

print(heart[0]+1, heart[1]+1)
print(left_arm, right_arm, waist.count('*'), left_leg, right_leg)