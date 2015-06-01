import math
def is_prime(x):
    count = 1
    while count < math.sqrt(x):
        count += 1
        if not x % count:
            return False
    return True

sum = 2
number = 3
while number < 2000000:
    if is_prime(number):
        sum += number
    number += 2

print sum