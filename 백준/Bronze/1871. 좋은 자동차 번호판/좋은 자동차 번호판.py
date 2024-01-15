import sys
input = sys.stdin.readline

char = [chr(i) for i in range(65, 91)]

for _ in range(int(input())):
    list_ = list(input().rstrip().split('-'))

    front = (char.index(list_[0][0]) * (26 ** 2)) + (char.index(list_[0][1]) * (26 ** 1)) + (char.index(list_[0][2]) * (26 ** 0))
    if abs(front - int(list_[1])) <= 100:
        print('nice')
    else:
        print('not nice')