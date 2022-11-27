a = [[1]*4]*3
b = [[1]*4 for i in range(3)]

a[1][1] = 2
b[1][1] = 2
print(a,b)