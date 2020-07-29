from math import ceil, sqrt

sum = 0
l = []
t = []


def count_factor(num):
    count = 0
    set = 1
    if (num < 100):
        count = 1
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                count += 1
                l.append(i)

        return count



    elif (ceil(sqrt(num)) != sqrt(num)):
        for i in range(2, ceil(sqrt(num)) + 1):
            if (num % i == 0):
                count += 1
                l.append(i)
        count = count * 2 + 1
        return count



    elif (ceil(sqrt(num)) == sqrt(num)):
        for i in range(2, ceil(sqrt(num)) + 1):
            if (num % i == 0):
                count += 1
                l.append(i)

        count = count * 2
        return count


for n in range(1, 1000000000):
    sum = n * (n + 1) // 2
    t.append(sum)

    if count_factor(sum) > 500:
        print("the least number with min of 500 factors is", sum)
        break
