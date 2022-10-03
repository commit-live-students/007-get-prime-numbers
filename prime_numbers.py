import math

def is_prime(n):
    if n == 1:
        return False

    if n == 2:
        return True
    
    if n > 2 and n % 2 == 0:
        return False

    max_divided_by = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_divided_by, 2):
        if n % i == 0:
            return False
    return True


def get_prime_numbers(value):
    primes = []
    for i in range(1, value + 1):
        if is_prime(i):
            primes.append(i)

    return primes
