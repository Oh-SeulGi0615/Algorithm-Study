s, e, a, no = 0, 0, 0, 0
for _ in range(int(input())):
    g, c, n = map(int, input().split())

    if g == 1:
        no += 1
    elif c < 3:
        s += 1
    elif c == 3:
        e += 1
    elif c == 4:
        a += 1

print(s, e, a, no, sep='\n')