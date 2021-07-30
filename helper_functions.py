import math


# checking prime or not
def isPrime(n):
    if n == 1:
        return 0
    k = math.ceil(n**0.5)
    for i in range(2, k+1):
        if n % i == 0:
            return 0
    return 1


# checking power of 2's
def isPowerOfTwo(n):
    return n & (n - 1)


# ordering the seats
def orderSeating(seating):
    prime = []
    power_of_2 = []
    other_ids = []
    for id in seating:
        if isPrime(id) == 1:
            prime.append(id)
        elif isPowerOfTwo(id) == 0 and id != 2:
            power_of_2.append(id)
        else:
            other_ids.append(id)
    new_seating = prime
    new_seating.extend(power_of_2)
    new_seating.extend(other_ids)
    return new_seating
