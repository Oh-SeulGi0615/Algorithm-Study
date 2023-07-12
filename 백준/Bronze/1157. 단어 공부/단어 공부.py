a = input()
b = a.upper()
c = [b[i] for i in range(len(b))]
d = list(set(c))
e = []

for j in range(len(d)):
    e.append(c.count(d[j]))

if e.count(max(e)) > 1:
    print('?')
else:
    print(d[e.index(max(e))])