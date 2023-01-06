def d(n):
    n = n + sum(map(int,str(n)))
    return n

notSelfNum = set()
for i in range(1, 10001):
    notSelfNum.add(d(i))

for j in range(1, 10001):
    if j not in notSelfNum:
        print(j)