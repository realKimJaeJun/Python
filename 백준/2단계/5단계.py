input_data = input().split(' ')

h = int(input_data[0])
m = int(input_data[1])

m -= 45
if m < 0:
    m += 60
    h -= 1

    if h < 0:
        h = 23
print(str(h) + ' ' + str(m))