from math import ceil, sqrt


def sum_of_prime(n):
    l = [2]
    for j in range(1, n):

        if (j < 50):
            for i in range(2, j):
                if (j % i == 0):
                    break
                if (i == j - 1):
                    l.append(j)
        else:
            for i in range(2, ceil(sqrt(j)) + 1):
                if (j % i == 0):
                    break
                if (ceil(sqrt(j))):
                    l.append(j)

    print(sum(l))


sum_of_prime(200000)
