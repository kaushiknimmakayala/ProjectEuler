import numpy as np


def proper_divisors_sum(a):
    b = []
    for i in range(1, a):
        if a % i == 0:
            b.append(i)
    return a, sum(b)


input = [proper_divisors_sum(n) for n in range(1, 10000)]

amicable_numbers = []
for i in range(0, len(input)):
    m = i + 1
    for j in range(m, len(input)):
        if input[i][0] == input[j][1] and input[i][1] == input[j][0]:
            print(input[i][0],input[i][1])
            amicable_numbers.append(input[i])

print(np.sum(amicable_numbers))

