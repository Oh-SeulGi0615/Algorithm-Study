n, k = map(int, input().split())

time = [0, 0, 0]
if k in time:cnt = 1
else: cnt = 0

while True:
  if (time[0] == n) and (time[1] == 59) and (time[2] == 59):
    break
  
  if time[2] == 59:
    time[1] += 1
    time[2] = 0
  else:
    time[2] += 1
  
  if time[1] == 60:
    time[0] += 1
    time[1] = 0
  
  string = str(time[0]).zfill(2) + str(time[1]).zfill(2) + str(time[2]).zfill(2)
  if str(k) in string:
    cnt += 1

print(cnt)