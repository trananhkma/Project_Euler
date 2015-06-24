import math


def is_prime(x):
    num = 1
    while num < math.sqrt(x):
        num += 1
        if not x % num:
            return False
    return True


primes = [2]
number = 3
while number < 10000:
    if is_prime(number):
        primes.append(number)
    number += 2

cumulative = {}
for i in range(len(primes)):
    cumulative[primes[i]] = sum(primes[:i+1])

max_ = 0
count = 0
for i in cumulative:
    for j in cumulative:
        temp = cumulative[j] - cumulative[i]
        if 1000000 > temp > max_ and is_prime(temp):
            count_tmp = primes.index(j) - primes.index(i)
            if count_tmp > count:
                max_ = temp
                count = count_tmp

print max_, count
