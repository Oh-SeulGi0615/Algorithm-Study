a, b = map(int, input().split())
turn = 1

while True:
    if turn == 1:
        b += a
        turn = 2
    else:
        a += b
        turn = 1

    if a >= 5 or b >= 5:
        break

if a >= 5:
    print('yj')
elif b >= 5:
    print('yt')