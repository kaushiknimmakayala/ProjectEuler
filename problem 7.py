from math import ceil, sqrt

l = [2]
for num in range(1, 2000000):
    if num > 1:
        for i in range(2, ceil(sqrt(num)) + 1):
            if (num % i) == 0:
                break
        else:
            l.append(num)

print(l[10000])
