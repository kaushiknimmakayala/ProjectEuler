sum = 0
f = [1,2]

for n in range(2, 1000):
    f.append(f[n-1]+f[n-2])
    if(f[n-1])>4000000:
        break



for i in f:
    if(i%2 ==0 and i<4000000):
        sum += i

print(sum)