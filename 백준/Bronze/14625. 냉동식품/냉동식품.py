sh, sm = map(int, input().split())
eh, em = map(int, input().split())
num = int(input())

now_h, now_m = sh, sm
cnt = 0
while True:
  if ((now_h * 60) + now_m) > ((eh * 60) + em):
    break

  if str(num) in str(now_h).zfill(2) or str(num) in str(now_m).zfill(2):
    cnt += 1

  if now_m < 59:
    now_m += 1
  else:
    now_h += 1
    now_m = 0

print(cnt)