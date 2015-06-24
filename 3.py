import math
def is_prime(x):
    count = 1
    while count < math.sqrt(x):
        count += 1
        if not x % count:
            return False
    return True

number = 3
temp_num = 600851475143

while number < temp_num:
    if is_prime(number) == True:
        if not temp_num % number:
            temp_num /= number
        number += 2
    else:
        number += 2

print number


#6857

