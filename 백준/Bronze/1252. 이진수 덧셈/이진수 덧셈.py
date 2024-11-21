sum = sum(list(map(lambda x: int(x, 2), input().split())))

print(str(bin(sum))[2:])