n = int(input())
arr = input().split()

can_play = True
last = ''

for i in range(len(arr)):
    if i == 0:
        last = arr[i][-1]
    else:
        if arr[i][0] == last:
            last = arr[i][-1]
        else:
            can_play = False

if can_play == True:
    print(1)
else:
    print(0)