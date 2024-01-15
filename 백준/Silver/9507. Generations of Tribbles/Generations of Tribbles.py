import sys
input = sys.stdin.readline

koong_ = {i:0 for i in range(70)}

koong_[0], koong_[1], koong_[2], koong_[3] = 1, 1, 2, 4

for j in range(4, 70):
    koong_[j] = koong_[j-1] + koong_[j-2] + koong_[j-3] + koong_[j-4]

for _ in range(int(input())):
    n = int(input())
    print(koong_[n])