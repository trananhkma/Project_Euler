# -*- coding: utf-8 -*-
import math
import time

start = time.time()

def is_prime(x):
    count = 1
    while count < math.sqrt(x):
        count += 1
        if not x % count:
            return False
    return True

primes = [2]

number = 3
while number < 1000:
    if is_prime(number):
        primes.append(number)
    number += 2


# Phân tích thành thừa số nguyên tố:
def dividetomax(p, n):
    # Tìm số mũ cao nhất của p khi lấy n chia p
    k = 0
    while True:
        if n % p:
            return p,k
        k += 1
        n /= p


def primefact(primes, n):
    tmp = map (dividetomax, primes, len(primes)*[n])
    tmp = filter(lambda i: i[1] > 0, tmp)
    return tmp


if __name__ == '__main__':
    n = 1000
    lst = []
    while True:
        tmp = primefact(primes, n)
        if len(tmp) == 4:
            lst.append(n)
        if len(lst) > 4:
            lst.remove(lst[0])
            if lst[3] == lst[2] + 1 == lst[1] + 2 == lst[0] + 3:
                print lst[0]
                break
        n += 1
    print time.time() - start
