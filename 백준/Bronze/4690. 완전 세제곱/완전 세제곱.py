for a in range(101):
    for b in range(2, 98):
        for c in range(b+1, 99):
            for d in range(c+1, 100):
                if (a ** 3) == (b ** 3) + (c ** 3) + (d ** 3):
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')