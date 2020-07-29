
def div_by_35(n):
    return sum([i for i in range(1,n) if(cond(n))])
def cond(n):
    return n % 3 == 0 or n % 5 == 0




print (div_by_35(1000))