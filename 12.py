# -*- coding: utf-8 -*-
# 500 = 2 * 2 * 5 * 5 * 5
# x = a**(2-1) + b**(2-1) + c**(5-1) + d**(5-1) + e**(5-1)
# ==> MINx = 2**4 * 3**4 * 5**4 * 7 * 11 = 62370000

import math

def is_prime(x):
    count = 1
    while count < math.sqrt(x):
        count += 1
        if not x % count:
            return False
    return True

prime_list = [2]

number = 3
while number < 1000:
    if is_prime(number):
        prime_list.append(number)
    number += 2

# Phân tích thành thừa số nguyên tố:
def dividetomax(p,m):
    # Tìm số mũ cao nhất của p khi lấy m chia p
    k = 0
    while True:
        if m % p:
            return (p,k)
        k += 1
        m /= p

def primefact(primes, n):
    tmp = map (dividetomax, primes, len(primes)*[n])
    tmp = filter(lambda u: u[1] > 0, tmp)
    return tmp


# Tìm số thuộc dãy tăng:
count = 2
num = 1
while True:
    num += count
    count += 1
    if num < 62370000:
        continue
    temp = primefact(prime_list, num)
    divs = 1     # Số lượng các ước của num
    for i in temp:
        divs *= (i[1] + 1)
    if divs > 500:
        print num 
        break

# 76576500
