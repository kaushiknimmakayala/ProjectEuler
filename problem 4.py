def pallin(n):
    flag = n
    new = 0
    r = 0
    while (n > 0):
        r = n % 10
        new = new * 10 + r
        n = n // 10

    n = flag
    if(n == new):
        return True
    else:
        return False

l = list()

for i in range(100,1000):
    for j in range(100,1000):
        if(pallin(i*j)==True):
            l.append(i*j)

print(max(l))