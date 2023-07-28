import sys
input = sys.stdin.readline

n = int(input())

for x in range(1,n+1):
    arr = list(map(int, input().split()))

    a = int(9.23076 * ((26.7 - arr[0]) ** 1.835))
    b = int(1.84523 * ((arr[1] - 75) ** 1.348))
    c = int(56.0211 * ((arr[2] - 1.5) ** 1.05))
    d = int(4.99087 * ((42.5 - arr[3]) ** 1.81))
    e = int(0.188807 * ((arr[4] - 210) ** 1.41))
    f = int(15.9803 * ((arr[5] - 3.8) ** 1.04))
    g = int(0.11193 * ((254 - arr[6]) ** 1.88))

    sum_ = a + b + c + d + e + f + g
    print(sum_)