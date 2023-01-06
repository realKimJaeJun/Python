i = int(input())
k = int(input())

if i > 0 and k > 0:
    print('1')
elif i < 0 and k > 0:
    print('2')
elif i < 0 and k < 0:
    print('3')
else:
    print('4')