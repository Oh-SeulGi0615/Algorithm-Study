import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

def check(list):
    dict_ = {0:100, 1:100, 2:200, 3:200, 4:300, 5:300, 6:400, 7:400, 8:500}
    for i in range(9):
        if list[i] > dict_[i]:
            return True
    return False

if check(arr) == False and sum(arr) >= 100:
    print('draw')
elif check(arr) == False and sum(arr) < 100:
    print('none')
elif check(arr) == True:
    print('hacker')