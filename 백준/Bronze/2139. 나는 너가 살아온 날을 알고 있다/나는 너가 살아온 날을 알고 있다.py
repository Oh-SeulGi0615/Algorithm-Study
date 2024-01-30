import sys
input = sys.stdin.readline

def check(num):
    if num % 4 == 0:
        if num % 400 == 0:
            return True
        elif num % 100 == 0:
            return False
        else:
            return True
    else:
        return False
    
day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

while True:
    d, m, y = map(int, input().split())
    if d == m == y == 0:
        break

    result = d
    for i in range(1, m):
        result += day[i]
    
    if check(y) == True and m > 2:
        result += 1

    print(result)