finger = {i:set() for i in range(1, 6)}

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    finger[a].add(b)
    finger[b].add(a)

if (finger[1] == set([3,4])) and (finger[3] == set([1,4])) and (finger[4] == set([1,3])) and (finger[2] == set([])) and (finger[5] == set([])):
    print('Wa-pa-pa-pa-pa-pa-pow!')
else:
    print('Woof-meow-tweet-squeek')