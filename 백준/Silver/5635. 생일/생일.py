import sys
input = sys.stdin.readline

name1, day1, month1, year1 = '', 0, 0, 0
name2, day2, month2, year2 = '', 0, 0, 0

for i in range(int(input())):
    arr = list(input().split())
    if i == 0:
        name2, day2, month2, year2 = arr[0], int(arr[1]), int(arr[2]), int(arr[3])
    name, day, month, year = arr[0], int(arr[1]), int(arr[2]), int(arr[3])
    
    if (year > year1) or (year == year1 and month > month1) or (year == year1 and month == month1 and day > day1):
        year1 = year
        month1 = month
        day1 = day
        name1 = name
    
    elif (year < year2) or (year == year2 and month < month2) or (year == year2 and month == month2 and day < day2):
        year2 = year
        month2 = month
        day2 = day
        name2 = name
    
print(name1)
print(name2)