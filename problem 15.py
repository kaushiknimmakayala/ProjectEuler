def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    return fact

def bc(a, b):
    return (fact(a+b)//(fact(a)*fact(b)))
def path(a,b):
    paths = bc(a, b)
    return paths

print(path(20,20))