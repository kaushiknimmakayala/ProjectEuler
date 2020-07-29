def sumsquare(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    total = sum * sum
    return total

def squaresum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i
    total = sum
    return total

print(sumsquare(100)-squaresum(100))


