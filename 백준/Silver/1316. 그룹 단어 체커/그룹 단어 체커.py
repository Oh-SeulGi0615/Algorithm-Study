N = int(input())

count = 0
for x in range(N):
    a = input()
    list_a = list(a)

    result1 = []
    for val in list_a:
        if val not in result1:
            result1.append(val)

    result2 = []
    result2.append(list_a[0])
    for i in range(1, len(list_a)):
        if list_a[i-1] != list_a[i]:
            result2.append(list_a[i])

    if result1 == result2:
        count += 1

print(count)