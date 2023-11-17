import sys
input = sys.stdin.readline

for _ in range(int(input())):
    t, w = map(int, input().split())
    bmi = w / ((t / 100) ** 2)

    if t < 159:
        if t <= 140:
            print(6)
        elif t < 146:
            print(5)
        else:
            print(4)
    elif 159 <= t < 161:
        if bmi < 16.0 or 35.0 <= bmi:
            print(4)
        else:
            print(3)
    elif 161 <= t < 204:
        if bmi < 16.0 or 35.0 <= bmi:
            print(4)
        elif 16.0 <= bmi < 18.5 or 30.0 <= bmi < 35.0:
            print(3)
        elif 18.5 <= bmi < 20.0 or 25.0 <= bmi < 30.0:
            print(2)
        else:
            print(1)
    else:
        print(4)