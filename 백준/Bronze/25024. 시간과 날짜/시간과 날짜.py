import sys
input = sys.stdin.readline

month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    answer = ['', '']
    
    if 0 <= x <= 23 and 0 <= y <= 59:
        answer[0] = 'Yes'
    else:
        answer[0] = 'No'

    if 1 <= x <= 12 and 1 <= y <= month[x]:
        answer[1] = 'Yes'
    else:
        answer[1] = 'No'
    
    print(*answer)