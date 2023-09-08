import sys
input = sys.stdin.readline

arr = list(input().split())

def cal(arr):
    if arr[1] == '+':
        result = int(arr[0]) + int(arr[2])
    elif arr[1] == '-':
        result = int(arr[0]) - int(arr[2])
    elif arr[1] == '*':
        result = int(arr[0]) * int(arr[2])
    else:
        if int(arr[0]) < 0 or int(arr[2]) < 0:
            result = -1 * (abs(int(arr[0])) // abs(int(arr[2])))
        else:
            result = abs(int(arr[0])) // abs(int(arr[2]))
    return result

cal1 = cal([cal(arr[0:3])] + arr[3:])
cal2 = cal(arr[:2] + [cal(arr[2:])])

print(min(cal1, cal2))
print(max(cal1, cal2))