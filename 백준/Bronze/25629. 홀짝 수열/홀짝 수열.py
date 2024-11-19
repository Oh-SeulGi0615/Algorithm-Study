n = int(input())
arr = list(map(int, input().split()))

even, odd = [i for i in arr if i % 2 == 0], [i for i in arr if i % 2 == 1]

if n % 2 == 0:
    if len(even) == len(odd) == (n // 2):
        print(1)
    else:
        print(0)
else:
    can_odd_len = (n // 2) + 1
    can_even_len = (n // 2)
    if (len(even) == can_even_len) and (len(odd) == can_odd_len):
        print(1)
    else:
        print(0)