import math

n = int(input())
arr = list(map(int, input().split()))

if len(arr) == 1:
    print(arr[0])

elif len(arr) == 2:
    gcd = math.gcd(arr[0], arr[1])
    result = int(arr[0] / gcd) * int(arr[1] / gcd) * gcd
    if result > 10**9:
        result = 10**9
        
    print(result)

else:
    gcd = math.gcd(arr[0], arr[1])
    result = int(arr[0] / gcd) * int(arr[1] / gcd) * gcd
    if result > 10**9:
        result = 10**9

    for i in range(2, len(arr)):
        gcd = math.gcd(result, arr[i])
        result = int(result / gcd) * int(arr[i] / gcd) * gcd
        if result > 10**9:
            result = 10**9

    print(result)