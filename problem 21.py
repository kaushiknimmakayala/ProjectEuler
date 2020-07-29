from math import ceil, sqrt


def sum_of_facts(n):
    l = []
    for i in range(1, n // 2 + 1):
        if (n % i == 0):
            l.append(i)
    return sum((int(i) for i in l))


x = []

for i in range(1, 1000):
    for n in range(1, 1000):
        if sum_of_facts(i) == n and sum_of_facts(n) == i:
            if (n == i):
                continue
            else:
                print(i)
                x.append(i)
print(x)
print(sum((int(i) for i in x)))
#35626