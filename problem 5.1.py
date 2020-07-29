def lcm(t,n):
    if(n>0):
        if not (t%n):
            if lcm(t,n-1):
                return True
            else:
                return False
        else:
            return False
    else:
        return True

i = 20
while not lcm(i,20):
    i+=20

print(i)