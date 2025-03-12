while True:
  try:
    spots = list(map(float, input().split()))

    a1 = spots[0:2]
    a2 = spots[2:4]
    b1 = spots[4:6]
    b2 = spots[6:8]

    h = a2[0] - a1[0]
    v = a2[1] - a1[1]

    if a2 == b1:
      print(f'{(b2[0] - h):.3f}', f'{(b2[1] - v):.3f}')
    elif a2 == b2:
      print(f'{(b1[0] - h):.3f}', f'{(b1[1] - v):.3f}')
    elif a1 == b1:
      print(f'{(b2[0] + h):.3f}', f'{(b2[1] + v):.3f}')
    elif a1 == b2:
      print(f'{(b1[0] + h):.3f}', f'{(b1[1] + v):.3f}')
  except:
    break