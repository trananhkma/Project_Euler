# -*- coding: utf-8 -*-

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

def sum_divs(x):
    sum_divs = 0
    for i in xrange(1, x):
        if not x % i:
            sum_divs += i
    return sum_divs

dict1 = {}
for i in xrange(2, 10000):
    if i in prime_list:
        continue
    else:
        temp = sum_divs(i)
        if temp in prime_list:
            continue
        else:
            temp2 = sum_divs(temp)
            if temp == temp2:
                continue
            if temp2 == i:
                dict1[i] = temp

# print dict1
# dict2 = dict1
# for i in dict2:
    # for j in dict2:
        # if dict2[j] == i:
            # del dict1[j]
    

print dict1

# 31626