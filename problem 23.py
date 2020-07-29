
l = []
a = []
def sum_of_div(n):
    for i in range(1,n // 2 + 1):
        if(n%i==0):
            l.append(i)

    return sum(int(i) for i in l)

print(sum_of_div(4))

def abnt(n):
    for i in range(1,n):
        if(i > sum_of_div(i)):
            print(i)
        else:
            continue

print(abnt(100))


