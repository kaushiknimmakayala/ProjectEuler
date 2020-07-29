def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    return fact


print(sum(int(i) for i in str(fact(100))))


