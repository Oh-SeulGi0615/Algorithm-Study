while True:
    try:
        string = input()

        a, b, c, d = 0, 0, 0, 0
        for i in string:
            if i == ' ': d += 1
            elif 97 <= ord(i) <= 122: a += 1
            elif 65 <= ord(i) <= 90: b += 1
            else: c += 1

        print(a, b, c, d)
    except EOFError:
        break