from math import ceil, sqrt

l = []
p = []


def prime(n):
    for i in range(2, ceil(sqrt(n)) + 1):
        if (n % i == 0):
            break
        if (i == ceil(sqrt(n))):
            return True


def largest_prime_fact(n):
    for i in range(2, ceil(sqrt(n)) + 1):
        if (n % i == 0):
            l.append(i)
    for i in l:
        if(prime(i)):
            p.append(i)


    print(p[-1])


largest_prime_fact(600851475143)
