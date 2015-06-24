import math
def is_prime(x):
    count = 1
    while count < math.sqrt(x):
        count += 1
        if not x % count:
            return False
    return True

count = 1
number = 3

while True:
    temple = is_prime(number)
    if temple == True:
        count += 1
        if count == 10001:
            print number
            break
    number += 2

#104743

