std = [False for i in range(30)]

for i in range(28):
    num = int(input())
    std[num-1] = True

for i in range(30):
    if not std[i]:
        print(i+1)