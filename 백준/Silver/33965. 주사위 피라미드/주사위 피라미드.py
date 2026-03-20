import sys
input = sys.stdin.readline

n = int(input())

noon_min = [0, 1, 3, 6, 10, 15]
noon_max = [0, 6, 11, 15, 18, 20]

dice_5 = 1
dice_4 = (n - 1) * 2
dice_3 = ((n - 2) * (n - 1)) // 2
dice_2 = n - 1
dice_1 = (n - 2) * (n - 1)

if n == 1:
  min_ = dice_5 * noon_min[5]
  max_ = dice_5 * noon_max[5]
  print(min_ + max_)

else:
  min_ = (dice_5 * noon_min[5]) + (dice_4 * noon_min[4]) + (dice_3 * noon_min[3]) + (dice_2 * noon_min[2]) + (dice_1 * noon_min[1])
  max_ = (dice_5 * noon_max[5]) + (dice_4 * noon_max[4]) + (dice_3 * noon_max[3]) + (dice_2 * noon_max[2]) + (dice_1 * noon_max[1])
  print(min_ + max_)