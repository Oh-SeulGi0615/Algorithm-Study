import sys
input = sys.stdin.readline

dict_ = {
    'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4,
    'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9
    }

color1 = input().rstrip()
color2 = input().rstrip()
color3 = input().rstrip()

cal1 = int(str(dict_[color1]) + str(dict_[color2]))
cal2 = cal1 * (10 ** dict_[color3])

print(cal2)