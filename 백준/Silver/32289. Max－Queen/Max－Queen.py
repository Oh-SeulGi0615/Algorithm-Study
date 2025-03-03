n, m = map(int, input().split())

row1 = 6 + (5 * (n-2))
other_row = (5 + (4 * (n-2))) * (m-2)

print(row1 + other_row)