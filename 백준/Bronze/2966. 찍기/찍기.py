import sys
input = sys.stdin.readline

n = int(input())
correct = list(input().rstrip())

adiran = ['A', 'B', 'C']
bruno = ['B', 'A', 'B', 'C']
goran = ['C', 'C', 'A', 'A', 'B', 'B']

s1, s2, s3 = 0, 0, 0
for i in range(len(correct)):
    if correct[i] == adiran[i%3]:
        s1 += 1
    if correct[i] == bruno[i%4]:
        s2 += 1
    if correct[i] == goran[i%6]:
        s3 += 1

print(max(s1, s2, s3))
if s1 == max(s1, s2, s3):
    print('Adrian')
if s2 == max(s1, s2, s3):
    print('Bruno')
if s3 == max(s1, s2, s3):
    print('Goran')