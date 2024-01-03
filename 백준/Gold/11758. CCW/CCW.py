import sys
input = sys.stdin.readline

arr = [list(map(int,input().split())) for _ in range(3)]

x1, x2, x3 = arr[0][0], arr[1][0], arr[2][0]
y1, y2, y3 = arr[0][1], arr[1][1], arr[2][1]

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3

if ccw(x1,y1,x2,y2,x3,y3) > 0:
    print(1)
elif ccw(x1,y1,x2,y2,x3,y3) < 0:
    print(-1)
else:
    print(0)