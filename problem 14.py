greatest = 0
l = []
max = 0


def sq(n):
    for i in range(1, ):
        if n % 2 == 0:
            l.append(n // 2)
            if n // 2 == 1:
                break
            else:
                sq(n // 2)
        if n % 2 != 0:
            l.append(3 * n + 1)
            sq(3 * n + 1)


for i in range(4, 1000000):
    sq(i)
    if len(l) > max:
        max = len(l)
        print(i, max)

    l.clear()

print(max)
