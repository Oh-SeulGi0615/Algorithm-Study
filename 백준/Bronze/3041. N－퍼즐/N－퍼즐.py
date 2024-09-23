puzzle = {'A':[0, 0],'B':[0, 1],'C':[0, 2],'D':[0, 3],'E':[1, 0],'F':[1, 1],'G':[1, 2],'H':[1, 3],'I':[2, 0],'J':[2, 1],'K':[2, 2],'L':[2, 3],'M':[3, 0],'N':[3, 1],'O':[3, 2]}

arr = []
for _ in range(4):
    s = list(input().rstrip())
    arr.append(s)

sum = 0
for i in range(4):
    for j in range(4):
        char = arr[i][j]
        if char == '.':
            continue
        x, y = puzzle[char][1], puzzle[char][0]
        sum += abs((i-y)) + abs((j-x))

print(sum)